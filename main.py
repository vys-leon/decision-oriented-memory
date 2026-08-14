from controller.controller import Controller
from llm.openrouter import OpenRouterLLM
from controller.system_prompt import SystemPrompt
from controller.prompt_builder import PromptBuilder
from memory.semantic_memory import SemanticMemory
from data_models.message import Message

def main():
    system_prompt = SystemPrompt()
    prompt_builder = PromptBuilder()
    long_memory = SemanticMemory()
    llm = OpenRouterLLM()
    controller = Controller(
        system_prompt=system_prompt,
        prompt_builder=prompt_builder,
        long_memory=long_memory,
        llm=llm
    )

    while True:
        user_message = input("User: ")
        user_message = Message(
            role='user',
            content=user_message
        )
        assistant_message = controller.process_message(user_message)
        print(assistant_message)
        inp = input("Продолжить (y/n)?")
        if inp == "n":
            break


if __name__ == "__main__":
    main()
