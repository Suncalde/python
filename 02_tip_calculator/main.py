print("Welcome to the tip Calculator.")

bill = float(input("What is the bill total $?"))
tip = int(input("What tip amount would you like to give? 10, 12, or 15?"))
num_people = int(input("How many people will split the bill?"))
tip_percent = tip/100
tip_total = bill * tip_percent
bill_total = bill + tip_total
bill_per_person = bill_total / num_people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
