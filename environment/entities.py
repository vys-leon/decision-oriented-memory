from dataclasses import dataclass
from typing import List

@dataclass
class WorldState:
    location: str
    object: str
    step: int