from environment.entities import Situation
from environment.scenarios import SCENARIOS
from environment.generation_options import CLASS_TO_ACTIONS
from environment.observation import ObservationGenerator
from environment.rules import RuleSet
from environment.generator import Generator

class TextWorld:
    def __init__(self, observation_generator: ObservationGenerator, rule_set: RuleSet):
        self.curr_step = 0
        self.curr_situation = SCENARIOS[self.curr_step]
        self.observation_generator = observation_generator
        self.rule_set = rule_set

    def reset(self):
        self.curr_step = 0

    def observe(self, generator: Generator):
        self.curr_situation = generator.generate_situation()
        observation = self.observation_generator.generate(self.curr_situation)
        available_actions = self.curr_situation.object.available_actions
        self.curr_step = self.curr_step + 1
        return observation, available_actions

    def step(self, action):
        feedback, reward = self.rule_set.evaluate(self.curr_situation, action)
        return feedback, reward


observation_generator = ObservationGenerator()
rule_set = RuleSet()
env = TextWorld(observation_generator, rule_set)
generator = Generator()

for i in range(10):
    generator.generate_object(rule_set=rule_set, class_="food")

print("Text sythetic environment")
cumm_reward = 0
env.reset()
while True:
    observation, available_actions = env.observe(generator)
    print(observation)
    for i in range(len(available_actions)):
        print(f"{i+1}) {available_actions[i]}")
    action = input("Input action (type q to quit the program): ")
    if action == "q":
        break
    while action not in available_actions:
        action = input("Incorrect action. Pick only actions from the list above: ")
        if action == "q":
            break
    if action == "q":
        break
    feedback, reward = env.step(action)
    cumm_reward += reward
    print(feedback)
    print(reward)
print("Cummulative reward: ", cumm_reward)