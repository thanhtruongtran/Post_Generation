import os
from langchain_community.llms import Replicate
from utils.logger_utils import get_logger
from config import EmbeddingModelConfig, LLMModelConfig
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from flasgger import Swagger

os.environ["REPLICATE_API_TOKEN"] =LLMModelConfig.MODEL_API


class EmbeddingModel:
    def __init__(self, model_name: str = None):
        if model_name == None:
            self._embed_model = HuggingFaceEmbedding(model_name=EmbeddingModelConfig.MODEL_NAME)
        else:
            self._embed_model = HuggingFaceEmbedding(model_name=model_name)

class LargeLanguageModel:
    def __init__(self, model_name: str = None, model_kwargs: dict = None):
        if (model_name == None) & (model_kwargs == None):
            self._embed_model = Replicate(
                model=LLMModelConfig.MODEL_NAME,
                model_kwargs=LLMModelConfig.MODEL_KWARGS,
            )
        elif (model_name != None) & (model_kwargs != None):
            self._embed_model = Replicate(
                model=model_name,
                model_kwargs=model_kwargs,
            )
        else:
            get_logger("Invalid initial input parameter")