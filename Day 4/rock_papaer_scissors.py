import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand_signs = ["Rock","Paper","Scissors"]
game_images = [rock,paper,scissors]
user_hand_sign = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors "))
computer_hand_sign = random.randint(0,2)

print(f"You Chose {hand_signs[user_hand_sign]}")
print(game_images[user_hand_sign])

print(f"Computer Chose {hand_signs[computer_hand_sign]}")
print(game_images[computer_hand_sign])


if(user_hand_sign == 0 and computer_hand_sign == 2) or (user_hand_sign == 2 and computer_hand_sign == 1) or (user_hand_sign == 1 and computer_hand_sign == 0):
    print("You Win")
elif(user_hand_sign == computer_hand_sign):
    print("Tie")
else:
    print("You Lose")

