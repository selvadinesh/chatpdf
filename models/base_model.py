
class Model:
    def __init__(self, temperature, model_name, embeddings):
        super().__init__()
        self.model_name = model_name
        self.temperature = temperature
        self.embeddings = embeddings

    # Common logic for generating a response
    def get_answer(self, messages) -> tuple[str, float]:
        pass