from dataclasses import dataclass
from typing import List, Literal
from enum import Enum

@dataclass
class Situation:
    location: str
    object: WorldObject

@dataclass
class WorldObject:
    id: int
    class_: str
    type: str
    available_actions: List[str]
    color: str | None
    poisonous: bool | None
    rotten: bool | None
    size: str | None
    strength: str | None
    is_container: bool | None
    is_weapon: bool | None