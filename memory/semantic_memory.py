from .base import Memory
from typing import List
from data_models.experience import Experience
import numpy as np
from .embeddings import Embeddings

class SemanticMemory(Memory):
  def __init__(self, embeddingModel: Embeddings):
    self.embeddingModel = embeddingModel
    self.memories = []
    self.max_memories = 100

  def addMemories(self, memories: List[str]):
    for memory in memories:
      embedding = self.embeddingModel.getEmbedding(memory)
      self.memories.append(embedding)
      if len(self.memories) > self.max_memories:
        self.memories.pop(0)

  def getMemories(self) -> np.ndarray:
    return np.array(self.memories)

  def saveToFileMemories(self):
    np.save("data/processed/semantic_memory.npy", np.array(self.memories))
