# Greeting the user
print("Welcome to Bill Split Calculator\nNo More Daunting Calculation")
# Storing the Total Bill
total_bill = float(input("What was the total bill? $"))
# Storing Tip Percentage To Give To Waiter
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# Storing No Of People To Split the Bill Into
no_of_people_to_split = int(input("How many people to split the bill? "))
# Using Formula Total Bill * 1.(Tip Percentage) / No Of People To Split the Bill
bill_per_person = (total_bill * (1 + (tip_percentage/100))) / no_of_people_to_split
# Rounding it off to 2 decimal places
bill_per_person = round(bill_per_person,2)
# Showing the result to the user
print(f"Each person should pay: ${bill_per_person}")



