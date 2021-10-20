#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
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
