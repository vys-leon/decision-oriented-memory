from environment.entities import Situation, WorldObject

SCENARIOS = [
    Situation(
        location="forest",
        object=WorldObject(
            name="red mushroom",
            description="red mushroom",
            hidden_property="poisonous",
            available_actions=["eat", "leave"]
        ),
        feedback={
            "eat": "The mushroom is poisonous. You are poisoned.",
            "leave": "You leave the mushroom alone."
        },
        reward={
            "eat": -1,
            "leave": 0
        }
    ),

    Situation(
        location="cave",
        object=WorldObject(
            name="cave red mushroom",
            description="red mushroom",
            hidden_property="edible",
            available_actions=["eat", "leave"]
        ),
        feedback={
            "eat": "The mushroom is healing you.",
            "leave": "You leave the mushroom alone."
        },
        reward={
            "eat": 1,
            "leave": 0
        }
    ),

    Situation(
        location="dungeon",
        object=WorldObject(
            name="strange chest",
            description="chest with a chain",
            hidden_property="Mimic",
            available_actions=["open", "leave"]
        ),
        feedback={
            "open": "You tried to open the chest, but it was a mimic - so you were attacked.",
            "leave": "You leave the chest alone."
        },
        reward={
            "open": -2,
            "leave": 0
        }
    ),

    Situation(
        location="dungeon",
        object=WorldObject(
            name="locked chest",
            description="chest",
            hidden_property="Good loot",
            available_actions=["open", "leave"]
        ),
        feedback={
            "open": "You tried to open the chest. The lock turned out to be worn and gave way quite easily. "
            "The chest turned out to contain a lot of useful loot.",

            "leave": "You leave the chest alone."
        },
        reward={
            "open": 2,
            "leave": 0
        }
    ),

    Situation(
        location="dungeon",
        object=WorldObject(
            name="slime",
            description="fearsome-looking slime",
            hidden_property="weak",
            available_actions=["attack", "run"]
        ),
        feedback={
            "attack": "You attacked the slime. It was pretty weak and you gained some expirience from it.",

            "run": "You decided to run away from a monster."
        },
        reward={
            "attack": 2,
            "run": 0
        }
        
    ),

    Situation(
        location="hell",
        object=WorldObject(
            name="ifrit",
            description="flying monster shooting fire",
            hidden_property="strong",
            available_actions=["attack", "run"]
        ),
        feedback={
            "attack": "You attacked the ifrit. But it was too strong for you - "
            "so you lost a lot of hp and almost died but you escaped from the monster",

            "run": "You decided to run away from a monster."
        },
        reward={
            "attack": -2,
            "run": 1
        }
    )
    # Situation(
    #     location="town",
    #     object="villager",
    #     hidden_property="peaceful"
    # ),

    # Situation(
    #     location="hell",
    #     object="piglin",
    #     hidden_property="peaceful"
    # ),

    # Situation(
    #     location="forest",
    #     object="wood",
    #     hidden_property="useful"
    # ),

    # Situation(
    #     location="forest",
    #     object="red berry",
    #     hidden_property="edible"
    # )
]