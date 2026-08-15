from environment.entities import Situation
from environment.scenarios import SCENARIOS
from environment.actions import ACTIONS
from environment.observation import ObservationGenerator

class TextWorld:
    def __init__(self, observation_generator: ObservationGenerator):
        self.curr_step = 0
        self.curr_situation = SCENARIOS[self.curr_step]
        self.observation_generator = observation_generator

    def reset(self):
        self.curr_step = 0

    def observe(self):
        self.curr_situation = SCENARIOS[self.curr_step]
        observation = self.observation_generator.generate(self.curr_situation)
        available_actions = self.curr_situation.object.available_actions
        self.curr_step = (self.curr_step + 1) % len(SCENARIOS)
        return observation, available_actions

    def step(self, action):
        feedback = self.curr_situation.feedback[action]
        reward = self.curr_situation.reward[action]
        return feedback, reward


observation_generator = ObservationGenerator()
env = TextWorld(observation_generator)

print("Text sythetic environment")
cumm_reward = 0
env.reset()
while True:
    observation, available_actions = env.observe()
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