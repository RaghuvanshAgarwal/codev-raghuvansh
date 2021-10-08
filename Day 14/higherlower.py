import random
import art 
from game_data import data


def get_random_entity(exception_entity = None):
    entity = random.choice(data)
    if exception_entity != None:
        is_unique_entity = False
        while not is_unique_entity:
            entity = random.choice(data)
            if entity != exception_entity:
                is_unique_entity = True
    return entity

def print_ui(entity1,entity2):
    


def main_function():
    score = 0
    entity1 = get_random_entity()
    entity2 = get_random_entity(entity1)
    