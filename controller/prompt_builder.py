from data_models.message import Message

class PromptBuilder:
    def __init__(self):
        self.prompt = {"messages": []}


    def get_prompt(self) -> dict:
        return self.prompt

    def create_prompt(self, 
                      long_memory_messages: list[Message], 
                      current_message: Message,
                      system_prompt: Message) -> dict:
        self.clear_prompt()
        self.prompt["messages"].append(
            {
                "role": system_prompt.role,
                "content": system_prompt.content
            }
        )

        for message in long_memory_messages:
                    self.prompt["messages"].append(
                        {
                            "role": message.role,
                            "content": [
                                {
                                    "type": "text",
                                    "text": message.content,
                                }
                            ]
                        }
                    )

        self.prompt["messages"].append(
             {
                  "role": current_message.role,
                  "content": [
                       {
                            "type": "text",
                            "text": current_message.content,
                            }
                            ]
                            }
                            )

        return self.prompt
    def clear_prompt(self):
        self.prompt = {"messages": []}