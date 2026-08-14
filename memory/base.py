from abc import ABC, abstractmethod
from typing import List
from data_models.experience import Experience
import numpy as np

class Memory(ABC):
  @abstractmethod
  def addMemories(self, memories: List[str]) -> None:
    pass
  @abstractmethod
  def getMemories(self) -> np.ndarray:
    pass
  @abstractmethod
  def saveToFileMemories(self) -> None:
    pass