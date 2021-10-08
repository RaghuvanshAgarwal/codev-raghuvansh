print("Welcome To Treasure Island\nYour Mission is to find the treasure.")
user_choice = ""
user_choice = input("You Reached a Dead End,\nWhere do you want to go 'left' or 'right'\n")
if (user_choice == "left"):
    user_choice = input("You are at the bank of river,\nYou want to 'wait' or 'swim'\n")
    if (user_choice == "wait"):
        user_choice = input("You Reached at three Mystery Door,\nWhich one you want to open 'red', 'yellow', or 'blue'\n")
        if(user_choice == "red"):
            print("Burned by fire.\nGame Over.")
        elif(user_choice == "yellow"):
            print('''  
  _________________.---.______
 (_(______________(_o o_(____()
              .___.'. .'.___.
              \ o    Y    o /
               \ \__   __/ /
                '.__'-'__.'
                    '''
                )
            print("You Win\nYou found the TREASURE")
        elif(user_choice == "blue"):
            print("Eaten by beasts.\nGame Over.")
        else:
            print("Game Over")
    else:
        print("Attacked by trout.\nGame Over")
else:
    print("Fall in to a hole.\nGame Over")


