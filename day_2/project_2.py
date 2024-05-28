# Tip Calculator
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
tip_on_bill = (total_bill*tip)/100
final_bill = total_bill + tip_on_bill
split_per_person = int(input("How many people to split the bill? "))
bill_per_person = round(final_bill/split_per_person, 2)
print(f"Each person should pay: ${bill_per_person}")