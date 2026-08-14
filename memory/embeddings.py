import requests
import json
import os
from dotenv import load_dotenv
import numpy as np

class Embeddings():
    def __init__(self):
       load_dotenv()

    def getEmbedding(self, input: str):
       response = requests.post(
          url="https://openrouter.ai/api/v1/embeddings",
          headers={
             "Authorization": "Bearer " + str(os.getenv("OPENROUTER_API_KEY")),
             "Content-Type": "application/json"
             },
             data=json.dumps({
                "model": "qwen/qwen3-embedding-8b",
                "input": input,
                # "input": ["text1", "text2", "text3"], # batch embeddings also supported!
                "encoding_format": "float"
                })
        )
       response = response.json()
       response = response["data"][0]["embedding"]
       response = np.array(response)
       return response