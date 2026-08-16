from environment.entities import Situation, WorldObject

class RuleSet:
    def general_rules(self, object: WorldObject):
        if object.class_ == "food":
            if object.color in ["orange", "red"]:
                object.poisonous = True
            elif object.color in ["black"]:
                object.rotten = True
        return object

    def evaluate(self, situation: Situation, action: str):
        if situation.object.class_ == "food":
            if action == "leave":
                return f"You decided to leave this {situation.object.type} and walk away.", 0
            if situation.object.poisonous:
                return f"The {situation.object.type} had a strange taste - you got poisoned.", -2
            if situation.object.rotten:
                return f"The {situation.object.type} tasted terrible - it made you feel sick for a while.", -1
            return f"The {situation.object.type} turned out to be very tasty.", 1
        return "", 0
