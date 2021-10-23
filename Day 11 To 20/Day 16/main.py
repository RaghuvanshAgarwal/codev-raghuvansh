from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def refresh_screen():
    os.system("pause")
    os.system("cls")


os.system("cls")
should_continue = True
while should_continue:
    user_input = input(f"What would you like to order:  ({coffee_menu.get_items()}) : ")
    if user_input == "report":
        coffee_maker.report()
        refresh_screen()
    elif user_input == "off":
        print("Turning off Coffee Machine")
        should_continue = False
    else:
        coffee_choice = coffee_menu.find_drink(user_input)
        if coffee_choice:
            if coffee_maker.is_resource_sufficient(coffee_choice):
                money_machine.make_payment(coffee_choice.cost)
                coffee_maker.make_coffee(coffee_choice)
        refresh_screen()
