from environment.generation_options import *
import random
from environment.entities import Situation, WorldObject
from environment.rules import RuleSet

class Generator:
    def __init__(self):
        self.curr_id = 0
        self.seed = 42
        self.objects = []
    def generate_object(self, rule_set: RuleSet, class_=None, type=None):
        if class_ == None:
            class_ = random.choice(CLASSES_)
        if type == None:
            type = random.choice(CLASS_TO_TYPES[class_])
        properties = {}
        properties["class_"] = class_
        properties["type"] = type
        properties["available_actions"] = CLASS_TO_ACTIONS[class_]
        for property in CLASS_TO_PROPERTY[class_]:
            properties[property] = random.choice(PROPERTIES_OPTIONS[property])

        for property in PROPERTIES_OPTIONS.keys():
            if property not in properties.keys():
                properties[property] = None
                
        new_object = WorldObject(
            id=self.curr_id,
            class_=properties["class_"],
            type=properties["type"],
            available_actions=properties["available_actions"],
            color=properties["color"],
            poisonous=properties["poisonous"],
            rotten=properties["rotten"],
            size=properties["size"],
            strength=properties["strength"],
            is_container=properties["is_container"],
            is_weapon=properties["is_weapon"]
        )
        new_object = rule_set.general_rules(new_object)
        self.objects.append(new_object)
        self.curr_id += 1
        return new_object

    def generate_situation(self):
        location = random.choice(LOCATIONS)
        object_ = random.choice(self.objects)
        new_situation = Situation(
            location=location,
            object=object_
        )
        return new_situation