############DEBUGGING#####################

# Describe Problem
# Expected Output : You got it
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
# Expected Output : Dice Images Between 1 to 6
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# Play Computer
# Input : 1994 | Expected Output : You are a Gen Z.
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# Fix the Errors
# Current Output : Typecast Error 
# Input : 19
# Expected Output : You can drive at age 19
# age = input("How old are you?")
# if age > 18:
#   print("You can drive at age {age}.")


# Print is Your Friend
# Input Example : 78, 56
# Current Output : 0
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# Use a Debugger
# Current Output : [26]
# Expected Output : [2, 4, 6, 10, 16, 26]
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

