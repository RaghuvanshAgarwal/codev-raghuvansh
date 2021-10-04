from art import logo
import os

def add(n1,n2):
  return round(n1 + n2,2)

def sub(n1,n2):
  return round(n1 - n2,2)

def multiply(n1,n2):
  return round(n1 * n2,2)

def divide(n1,n2):
  return round(n1 / n2,2)

operators = {
  "+" : add,
  "-" : sub,
  "*" : multiply,
  "/" : divide,
}

def get_display_operators():
  operation_list = ""
  for operator in operators:
    operation_list +=  operator + "\t|\t"
  return (operation_list)




def calculator():
  should_continue = True
  os.system("cls")
  print(logo)
  num1 = float(input("Enter First Number : "))
  operation_symbol = input("Available Operators\t" + get_display_operators() + " :\t")
  num2 = float(input("Enter Second Number : "))
  while should_continue:
    function = operators[operation_symbol]
    result =  function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    user_input = input(f"Type 'y' to continue performing on {result},\nType 'n' to start fresh,\nType 'e' to exit : ")
    os.system("cls")
    print(logo)
    if user_input == "y":
      print(f"Continue performing on {result}")
      operation_symbol = input("Available Operators\t" + get_display_operators() + " :\t")
      num2 = float(input("Enter Second Number : "))
      num1 = result
    elif user_input == "n":
      calculator()
      break
    elif user_input == "e":
      should_continue = False
    
    



calculator()
print("Thank you for using PyCalculator")