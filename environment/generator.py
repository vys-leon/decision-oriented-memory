from .entities import WorldState

class WorldGenerator:
    def __init__(self):
        self.world = [
            WorldState(
                location="лес",
                object="красный гриб",
                step=1
            ),
            WorldState(
                location="лес",
                object="синий гриб",
                step=2
            ),
            WorldState(
                location="данж",
                object="старый сундук",
                step=3
            ),
            WorldState(
                location="опушка леса",
                object="яркая ягода",
                step=4
            ),
            WorldState(
                location="опушка леса",
                object="чёрная ягода",
                step=5
            ),
            WorldState(
                location="данж",
                object="запечатанный сундук",
                step=6
            ),
            WorldState(
                location="данж",
                object="сундук с цепочкой",
                step=7
            ),
            WorldState(
                location="данж",
                object="привидение",
                step=8
            ),
            WorldState(
                location="лес",
                object="слизняк",
                step=9
            ),
            WorldState(
                location="берег озера",
                object="оранжевая ягода",
                step=10
            ),
        ]