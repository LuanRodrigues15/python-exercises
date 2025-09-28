import random

option = ["rock", "paper", "scissors"]

while True:
    choiceComputer = random.choice(option)
    choiceUserIndex = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
    if choiceUserIndex < 0 or choiceUserIndex > 2:
        print("You typed an invalid number. You lose!")
        continue

    choiceUser = option[choiceUserIndex]

    print(f"Computer chose: {choiceComputer}")   
    print(f"You chose: {choiceUser}")   

    if choiceComputer == choiceUser:
        print("It's a draw")
 
    elif (choiceUser == "rock" and choiceComputer == "scissors") or \
        (choiceUser == "paper" and choiceComputer == "rock") or \
        (choiceUser == "scissors" and choiceComputer == "paper"):
        print("You win!")
    else:
        print("You lost!") 

    tryAgain = input("Try again? S/N: ")

    if tryAgain.upper() == "S":
        print("Ok, Good Luck!")
    else:
        break