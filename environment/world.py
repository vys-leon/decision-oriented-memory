from .entities import WorldState
from .generator import WorldGenerator

class TextWorld:
    def __init__(self):
        self.generator = WorldGenerator()
        self.state = self.generator.world[0]

    def reset(self):
        self.state = self.generator.world[0]

    def observe(self):
        pass

    def step(self, action):
        

