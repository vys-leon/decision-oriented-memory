from dataclasses import dataclass
from typing import List

@dataclass
class Experience:
  observation: str
  action: str
  feedback: str
  reward: int