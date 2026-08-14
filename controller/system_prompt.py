from data_models.message import Message

class SystemPrompt:
    def __init__(self):
        self.system_prompt = Message(
            role="system",
            content="""
            
            """
        )

    def get_system_prompt(self) -> Message:
        return self.system_prompt