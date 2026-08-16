ACTIONS = ["eat", "leave", "open", "attack", "run", "take"]
CLASSES_ = ["food", "monster", "human", "item"]
TYPES = ["berry", "mushroom", "vegetable", "fruit", 
        "slime", "frog", "ifrit", "skeleton", "spider", "zombie", "mimic",
        "villager",
        "chest", "sword"]

CLASS_TO_TYPES = {
    "food": ["berry", "mushroom", "vegetable", "fruit"],
    "monster": ["slime", "frog", "ifrit", "skeleton", "spider", 
                "zombie", "mimic"],
    "human": ["villager"],
    "item": ["chest", "sword"]
}

CLASS_TO_PROPERTY = {
    "food": ["color", "poisonous", "rotten"],
    "monster": ["color", "size", "strength"],
    "human": [],
    "item": ["is_container", "is_weapon"]
}

PROPERTIES_OPTIONS = {
    "color": ["orange", "blue", "red", "yellow", "purple", "black", "white"],
    "poisonous": [False],
    "rotten": [False],
    "size": ["small", "medium", "big", "giant"],
    "strength": ["weak", "normal", "strong"],
    "is_container": [False],
    "is_weapon": [False]
}

CLASS_TO_ACTIONS = {
    "food": ["eat", "leave"],
    "monster": ["attack", "run"],
    "human": ["attack", "leave"],
    "item": ["open", "take", "leave"]
}

LOCATIONS = ["forest", "hell", "dungeon", "cave", "plain"]