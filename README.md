

## How to run the ChatPDF (GUI mode)

Here the instructions to run LLM ChatBOT in GUI mode:

1. Git clone the repository on your local machine:
  ```
  git clone https://github.com/selvadinesh/chatpdf
  cd chatpdf
  ```

2. Download the LLama 2 model in the ```models``` folder:
  ```
  wget -P models/ https://huggingface.co/localmodels/Llama-2-7B-Chat-ggml/resolve/main/llama-2-7b-chat.ggmlv3.q2_K.bin
  ```

3. Create a Python Virtual environment in your current folder so that you don't corrupt the global python environment creating conflicts with other python applications:
  ```
  python3 -m venv venv
  ```

4. Activate the Python virtual environment:
  ```
  source venv/bin/activate
  ```

5. Install the Python libraries in your Python virtual environment:
  ```
  pip3 install -r requirements.txt
  ```

6. Run the LLM ChatBOT in GUI mode:
  ```
  streamlit run gui_app.py
  ```

## How to run the LLM ChatBOT (Text mode)

Here the instructions to run LLM ChatBOT in Text mode:

1. Run the step 1, 2, 3, and 4 of the previous section.

2. Run the LLM ChatBOT in Text mode:
  ```
  python3 text_app.py
  ```
![image](https://github.com/selvadinesh/chatpdf/assets/6970641/19b4b6ab-714a-4a64-89e4-64b39eeb4bb1)



