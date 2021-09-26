print("Welcome to Bill Split Calculator\nNo More Daunting Calculation")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_people_to_split = int(input("How many people to split the bill? "))
bill_per_person = (total_bill * (1 + (tip_percentage/100))) / no_of_people_to_split
bill_per_person = round(bill_per_person,2)
print(f"Each person should pay: ${bill_per_person}")



