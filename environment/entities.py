from dataclasses import dataclass
from typing import List

@dataclass
class Situation:
    location: str
    object: WorldObject
    feedback: dict[str, str]
    reward: dict[str, int]

@dataclass
class WorldObject:
    name: str
    description: str
    hidden_property: str
    available_actions: List[str]