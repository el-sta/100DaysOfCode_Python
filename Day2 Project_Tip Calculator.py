#Day2 Project: Tip Calculator

#Welcome message
print("Welcome to the tip calculator!")

#ask what was the bill
bill = float(input("What was the total bill?"))

#ask what percentage of tip they are willing to pay
tip_percent = int(input("How much tip would you like to give? 10, 12 or 15?"))

#ask how many people will split the bill
people = int(input("How many people to split the bill?"))

#calculate how much bill each of them will pay
person_bill = bill/people

#calculate how much tip each of them will pay 
person_tip = (bill*tip_percent/100)/people

#find final bill per person
person_final_bill = person_bill + person_tip

#round the final amount using 2 decimal points
person_final_bill = round(person_final_bill,2)

#print the answer
print(f"Each person should pay: {person_final_bill}")
