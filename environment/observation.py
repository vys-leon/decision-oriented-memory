from .entities import WorldState

class ObservationGenerator:
    def generate(self, state: WorldState) -> str:
        observation = "Ты находишься в " + state.location + \
        ". Ты замечаешь " + state.object + \
        ". Твои возможные действия: \n" + \
        "\n".join(state.actions) + \
        "\nВыбери действие и укажи его в ответе."
        return observation