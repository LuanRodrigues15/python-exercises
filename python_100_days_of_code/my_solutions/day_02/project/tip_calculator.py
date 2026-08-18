import math

print("Welcome to the tip calculator!")
totalBill = float(input("What was the total bill? $" ))
tip = float(input("How much tip would you like to give? 10, 12, or 15? " ))
numPeople = int(input("How many people to split the bill? " ))

result = ((totalBill * (1 + (tip / 100))) / numPeople)
print(f"Each person should pay: ${round(result,2)}")