import random
import os

number = random.randint(1,100)

start_game = True
while start_game:    
    print("Welcome to the Number Guessing Game!")
    game = input("Let's play? 'y' or 'n': ").lower()
    
    if game == 'n':
        print("Ok, thanks!")
        break
    
    os.system('cls')
    print("I'm thinking of a number between 1 and 100.")
    

    choose_difficulty = True
    while choose_difficulty:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == 'hard':
            attempts = 5
            break
        elif difficulty == 'easy':
            attempts = 10
            break
        else:
            print("Wrong, choose an existing difficulty")

    os.system('cls')
    while attempts >= 0:
        if attempts == 0:
            print(f"You lost! The answer was {number}")
            break
            
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        if guess == number:
            print(f"You got it! The answer was {number}")
            break
        elif guess > number:
            print("Too high.\nGuess again.")
        else:
            print("Too low.\nGuess again.")

        attempts -= 1