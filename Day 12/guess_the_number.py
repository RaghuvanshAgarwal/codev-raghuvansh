import random
import os
from art import logo


attempts_nr = 0
def greet_user():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def choose_difficulty_level():
    global attempts_nr
    print("Easy : 10 Attempts | Hard : 05 Attempts")
    user_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if user_input == "hard":
        attempts_nr = 5
        print(f"You Chose Hard Difficulty, You Have Now {attempts_nr} to guess the number, Good Luck!")
    elif user_input == "easy":
        attempts_nr = 10
        print(f"You Chose Easy Difficulty, You Have Now {attempts_nr} to guess the number, Take it Easy Man!")


def guess_again_info():
    global attempts_nr
    print(f"Guess Again!\nYou Have {attempts_nr} attempts left to guess the number")

def clear():
    os.system("cls")

def number_guess():
    global attempts_nr
    print(logo)
    actual_number = random.randint(1,100)
    guess_number = 0
    greet_user()
    choose_difficulty_level()
    end_game = False
    while not end_game:
        if attempts_nr > 0:
            guess_number = int(input("Make a Guess : "))
            if guess_number > actual_number:
                print("Too High")
                attempts_nr -=1
                guess_again_info()
            elif guess_number < actual_number:
                print("Too Low")
                attempts_nr -=1
                guess_again_info()
            else:
                print(f"You guessed Corrrectly. The Number was {actual_number}")
                end_game = True
        else:
            end_game = True
            print(f"You Failed to Guess the Number. The Number was {actual_number}")
    
    user_input = input("Do you want to play again.Type 'yes' otherwise 'no' : ").lower()
    if user_input == "yes":
        clear()
        number_guess()


clear()
number_guess()
    