
import streamlit as st
from langchain.schema import (HumanMessage, AIMessage)
from models.base_model import Model
from ui.page import Page
from chatbot.chat_bot import ChatBOT
import tempfile
import os

# This class is responsible for displaying the ChatBOT page using Streamlit.
class ChatBotPage(Page):
    # Renders the ChatBOT page.
    def render(self):
        # Initialize the page with the title, header, and sidebar.
        self.__init_page()
        # Select the LLM model to use.
        self.__init_messages()

        # Supervise user input
        if user_input := st.chat_input("Input your question!"):
            with st.spinner("ChatPDF is typing ..."):
                _, _ = st.session_state.chatbot.get_answer(user_input)

        # Display chat history
        messages = st.session_state.chatbot.get_chat_history()
        for message in messages:
            if isinstance(message, AIMessage):
                with st.chat_message("assistant"):
                    st.markdown(message.content)
            elif isinstance(message, HumanMessage):
                with st.chat_message("user"):
                    st.markdown(self.__extract_userquesion_part_only(message.content))

        # Display the chat cost
        # costs = st.session_state.chatbot.get_chat_costs()
        # st.sidebar.markdown("## Costs")
        # st.sidebar.markdown(f"**Total cost: ${sum(costs):.5f}**")
        # for cost in costs:
        #     st.sidebar.markdown(f"- ${cost:.5f}")

    # Initialize the ChatBOT page
    def __init_page(self) -> None:
        st.set_page_config(
            page_title="ChatPDF"
        )
        st.header("PDF Upload")
        uploaded_file = st.file_uploader(label="Here, upload your PDF file you want ChatPDF to use to answer",
            type="pdf"
        )

        st.header("ChatPDF")
        st.sidebar.title("Options")
        chatbot = None
        if "chatbot" not in st.session_state:
            chatbot = ChatBOT()
            st.session_state.chatbot = chatbot
            # Load the PDF file in the LLM ChatBOT
        else:
            chatbot = st.session_state.chatbot
        if uploaded_file and "uploaded_file" not in st.session_state:
            with st.spinner("Loading PDF ..."):
                temp_dir = "pdfs"
                path = os.path.join(temp_dir, uploaded_file.name)
                with open(path, "wb") as f:
                    f.write(uploaded_file.getvalue())
                chatbot.upload_pdf(path)
                st.session_state.uploaded_file = uploaded_file
                st.success("File Loaded Successfully!!")

    # Select the ChatBOT LLM model
    def __select_model(self) -> Model:
        temperature = 0.0
        st.session_state.chatbot.set_model(ChatBOT.Model.LLAMA, temperature)

    # Clear the conversation
    def __init_messages(self) -> None:
        clear_button = st.sidebar.button("Clear Conversation", key="clear")
        if clear_button:
            st.session_state.chatbot.clear_conversation()

    def __extract_userquesion_part_only(self, content):
        """
        Function to extract only the user question part from the entire question
        content combining user question and pdf context.
        """
        content_split = content.split("[][][][]")
        if len(content_split) == 3:
            return content_split[1]
        return content