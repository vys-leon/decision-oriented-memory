from .system_prompt import SystemPrompt
from .prompt_builder import PromptBuilder
from memory.base import Memory
from llm.base import LLM
from data_models.message import Message

class Controller:
    def __init__(self,
                 system_prompt: SystemPrompt,
                 prompt_builder: PromptBuilder,
                 long_memory: Memory,
                 llm: LLM):
        self.system_prompt = system_prompt
        self.prompt_builder = prompt_builder
        self.long_memory = long_memory
        self.llm = llm

    def process_message(self, message: Message) -> Message:
        prompt = self.prompt_builder.create_prompt(
            self.long_memory.get_history(),
            message,
            self.system_prompt.get_system_prompt()
        )
        response = self.llm.generate(prompt)
        self.long_memory.add(message)
        self.long_memory.add(response)
        return response
    