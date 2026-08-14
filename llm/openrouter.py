import requests
import json
import os
from dotenv import load_dotenv
from .base import LLM
from data_models.message import Message

class OpenRouterLLM(LLM):
    def __init__(self):
       load_dotenv()

    def generate(self, prompt: dict) -> Message:
       response = requests.post(
          url="https://openrouter.ai/api/v1/chat/completions",
          headers={
             "Authorization": "Bearer " + str(os.getenv("OPENROUTER_API_KEY"))
             },
             data=json.dumps({
                "model": "qwen/qwen3.7-plus",
                "session_id": "decision-oriented-memory",
                "messages": prompt["messages"],
                "reasoning": {"enabled": False}
                })
        )
       response = response.json()
       response = response['choices'][0]['message']['content']
       response = Message(
          role="assistant",
          content=response
       )
       return response