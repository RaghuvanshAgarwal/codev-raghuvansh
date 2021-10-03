import os
from art import logo

bidders_dictionary = {}

def add_new_bidder():
    name = input("Enter Name Of Bidder : ")
    amount = float(input(f"Amount {name} wants to Bid : $"))
    bidders_dictionary[name] = amount

def clear_screen():
    os.system("cls")

# Main Logic
wants_to_continue = True
while wants_to_continue:
    clear_screen()
    print(logo)
    add_new_bidder()
    user_choice = input("Want to add more bidder?\nType 'yes' to continue, otherwise 'no' : ").lower()
    if user_choice == "no":
        wants_to_continue = False
        clear_screen()

highest_bidder = ""
highest_bidder_amount = 0
for bidder in bidders_dictionary:
    bidding_amount = bidders_dictionary[bidder]
    if bidding_amount > highest_bidder_amount:
        highest_bidder_amount = bidding_amount
        highest_bidder = bidder

print(logo)
print(f"{highest_bidder} won the secret auction, Bidding Amount is ${bidders_dictionary[highest_bidder]}")