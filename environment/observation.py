from .entities import Situation

class ObservationGenerator:
    def generate(self, situation: Situation) -> str:
        observation = f"""
You are in a {situation.location}.
You see a {situation.object.color + " " if situation.object.color else ""}{situation.object.size + " " if situation.object.size else ""}{situation.object.type}.
        """
        return observation