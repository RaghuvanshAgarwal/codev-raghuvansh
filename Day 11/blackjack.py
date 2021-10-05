rules = """############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################"""
import random
import os
from art import logo

user_cards = []
computer_cards = []


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(player_cards):
    score = 0
    for card in player_cards:
        score += card
    return score

def display_current_scores():
    print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

def display_all_cards():
    print(f"Your cards: {user_cards} | Score: {calculate_score(user_cards)}")
    print(f"Computer's cards: {computer_cards} | Score: {calculate_score(computer_cards)}")

def black_jack():
    os.system("cls")
    print(logo)
    user_cards.clear()
    computer_cards.clear()
    #Initial 2 Card Deals
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    display_current_scores()
    #Dealing all Computer Cards Internally untill score is above 17
    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    should_continue = True
    while should_continue:
        user_input = input("Type 'Y' to get another card, type 'N' to pass: ").lower()
        if user_input == "y":
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            os.system("cls")
            print(logo)
            if user_score >= 22:
                if 11 in user_cards:
                    if (user_score - 10) >=22:
                        should_continue = False
                    else:
                        index=user_cards.index(11)
                        user_cards.remove(11)
                        user_cards.insert(index,1)
                        user_score = calculate_score(user_cards)
                        display_current_scores()
                else:
                    should_continue = False
            else:
                display_current_scores()
        else:
            os.system("cls")
            print(logo)
            should_continue = False


    display_all_cards()
    
    if user_score <= 21:
        if computer_score <= 21:
            if user_score > computer_score:
                print("You Won")
            elif user_score == computer_score:
                print("Draw")
            else:
                print("You Lose")
        else:
            print("Dealer Went above 21, You Won")
    else:
        print("You Lose, You Went Above 21")

    user_input = input("Type 'Y' to play another match, Otherwise Type 'N' to exit : ").lower()
    if user_input == "y":
        black_jack()
        

os.system("cls")
print(rules)
user_input = input("Want to Play BlackJack : Type [Y/N] : ").lower()
if user_input == "y":
    black_jack()
else:
    print("Goodbye, Have a Nice Day")