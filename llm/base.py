from abc import ABC, abstractmethod
from data_models.message import Message

class LLM(ABC):
    @abstractmethod
    def generate(self, prompt: dict) -> Message:
        pass