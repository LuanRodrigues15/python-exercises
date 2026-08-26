'''
Human vs Computer Guess the number
'''

import random as rd

attempts_pc = 0
attempts_human = 0

def binary_search(list, item):
    attempts = 0
    low = 0
    high = len(list) - 1

    print("\nSpoiler: It will take a maximum of 7 attempts.\n")

    while low <= high:
        attempts += 1
        mid = (low + high) // 2
        guess = list[mid]
        print(f"Computer try {guess}")
        if guess == item:
            print(f"Number of attempts to Win: {attempts}")
            return attempts
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

def compareResults(attempts_pc, attempts_human):
    print(f"\nAttempts human: {attempts_human}\nAttempts PC: {attempts_pc}")
    if attempts_pc < attempts_human:
        print(f"PC wins with {attempts_pc} attempts")
    elif attempts_pc > attempts_human:
        print(f"Human wins with {attempts_human} attempts")
    else:
        print("It's a draw!")


list_numbers = list(range(1, 101))
number_to_guess = rd.randint(1, 100)
print(number_to_guess)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' for 10 attempts or 'hard' for 5 attempts: ").lower()

attempts = int (10 if difficulty == "easy" else 5)
print(f"You have {attempts} attempts remaining to guess the number.")
attempts_start = attempts

while attempts != 0:
    number = int(input("Make a guess: "))
    if number == number_to_guess:
        print("Congratulations, You Win!")
        attempts_human = attempts_start - attempts
        break
    elif number < number_to_guess:
        print("Too low.")
    else:
        print("Too high.")

    attempts -= 1
    print(f"You have {attempts} attempts remaining to guess the number.")

if attempts == 0:
    print("You've run out of guesses.")

print("\nIt's time for the PC to play!")
attempts_pc =binary_search(list_numbers, number_to_guess)
compareResults(attempts_pc, attempts_human)