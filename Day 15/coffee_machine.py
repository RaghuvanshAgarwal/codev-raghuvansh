from menu_data import MENU
import os

resources = {
    "water": 1000,
    "milk": 2000,
    "coffee": 1000,
}

account_balance = 0


def generate_report():
    global resources, account_balance
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    report = f"Water  : {water}ml\nMilk   : {milk}ml\nCoffee : {coffee}g\nMoney  : ${account_balance}"
    return report


def check_resources(coffee_type):
    global resources
    is_enough_resources = True
    ingredients = coffee_type["ingredients"]
    if "water" in ingredients:
        if resources["water"] < ingredients["water"]:
            is_enough_resources = False
            print("Sorry there is not enough water")
    if "milk" in ingredients:
        if resources["milk"] < ingredients["milk"]:
            is_enough_resources = False
            print("Sorry there is not enough milk")
    if "coffee" in ingredients:
        if resources["coffee"] < ingredients["coffee"]:
            is_enough_resources = False
            print("Sorry there is not enough coffee")
    return is_enough_resources

def process_coins():
    quaters = int(input("How many Quarters (Face Value $0.25) : "))
    dimes   = int(input("How many Dimes    (Face Value $0.10) : "))
    nickles = int(input("How many Nickles  (Face Value $0.05) : "))
    pennies = int(input("How many Pennies  (Face Value $0.01) : "))
    money_inserted = (quaters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    money_inserted = round(money_inserted,2)
    print(f"Money Inserted : ${money_inserted}")
    return money_inserted
    
def display_menu():
    menu = "What would you like? Type "
    menu_list = list(MENU)
    for index in range(0,len(menu_list)):
        if index == 0:
            menu += "(" + menu_list[index].capitalize() + "/"
        elif index == len(menu_list) - 1:
            menu += menu_list[index].capitalize() + ") : "
        else:
            menu += menu_list[index].capitalize() + "/"
    return menu


def deduct_resources(coffee_type):
    global resources 
    ingredients = coffee_type["ingredients"]
    if "water" in ingredients:
        resources["water"] -= ingredients["water"]
    if "milk" in ingredients:
       resources["milk"] -= ingredients["milk"]
    if "coffee" in ingredients:
        resources["coffee"] -= ingredients["coffee"]
    
    
def refresh_page():
   os.system("pause")
   os.system("cls") 
    

os.system("cls") 
should_continue = True
while should_continue:
    print("Administrative Input : Type 'report' | Type 'off'")
    user_input = input(display_menu()).lower()
    if user_input in MENU:
        if check_resources(MENU[user_input]):
            coffee_cost = MENU[user_input]["cost"]
            print(f"{user_input.capitalize()} will cost you : ${coffee_cost}")
            money_inserted =  process_coins()
            if money_inserted >= coffee_cost:
                account_balance += coffee_cost
                money_left = money_inserted - coffee_cost
                deduct_resources(MENU[user_input])
                if money_left > 0:
                    print(f"Here is your change ${round(money_left,2)}")
                print(f"Here, Enjoy your {user_input.capitalize()} ☕")
            else:
                print("Insufficient Money Inserted")
        refresh_page()
    elif user_input == "report":
        print(generate_report())
        refresh_page()
    elif user_input == "off":
        print("Turning off Machine")
        should_continue = False
    else:
        print("Invalid Input")

print("Machine Turned Off")
            
            