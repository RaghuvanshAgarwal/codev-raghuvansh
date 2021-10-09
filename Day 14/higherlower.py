import random
import os
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

def get_entity_statement(index,entity):
    name = entity["name"]
    description = entity["description"]
    country = entity["country"]
    statement = f"Compare {index}: {name}, a {description}, from {country}."
    return statement

def print_ui(entity1,entity2):
    print(get_entity_statement("A",entity1))
    print(art.vs)
    print(get_entity_statement("B",entity2))
    


def main_loop():
    score = 0
    entity1 = get_random_entity()
    end_game = False
    
    while not end_game:
        os.system("cls")
        print(art.logo)
        print(f"Current Score : {score}")
        entity2 = get_random_entity(entity1)
        print_ui(entity1,entity2)
        entity_1_follower_count = entity1["follower_count"]
        entity_2_follower_count = entity2["follower_count"]
        #print(f"Pstt, A: {entity_1_follower_count}, B: {entity_2_follower_count}")
        user_input = input("Who Has more followers? Type 'A' or 'B' : ").lower()
        if user_input == "a":
            if entity_1_follower_count > entity_2_follower_count:
                score += 1
                entity1 = entity2
            else:
                print(f"Wrong!!, Final Score {score}")
                end_game = True
        else:
            if entity_1_follower_count < entity_2_follower_count:
                score += 1
                entity1 = entity2
            else:
                print(f"Wrong!!, Final Score {score}")
                end_game = True
    
    
    


should_continue = True
main_loop()
while should_continue:
    user_input = input("Wish to Play Again, Type 'Y or 'N' : ").lower()
    if user_input == "y":
        main_loop()
    else:
        should_continue = False
print("Thank You for Playing Higher or Lower")