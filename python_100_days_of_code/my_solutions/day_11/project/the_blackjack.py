import random

all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game = True

def new_cards(cards, num):
    for i in range(num):
        new_card = random.choice(all_cards)

        if new_card == 11 and sum(cards) + 11 > 21:
            cards.append(1)
        else:
            cards.append(new_card)

def result(my_cards, pc_cards):
    total_my_cards = sum(my_cards)
    total_pc_cards = sum(pc_cards)

    print(f"\nYour final hand: {my_cards}, final score: {total_my_cards}")
    print(f"Computer's final hand: {pc_cards}, final score: {total_pc_cards}")

def check_winner(my_cards, pc_cards, final=False):
    total_my_cards = sum(my_cards)
    total_pc_cards = sum(pc_cards)
    message = None

    if total_my_cards > 21:
        message = "You went over. You lose."
    elif total_pc_cards > 21:
        message = "PC went over. You win!"
    elif final: 
        if total_my_cards == total_pc_cards:
            message = "It was a draw!"
        elif total_my_cards > total_pc_cards:
            message = "You lose!"
        else:
            message = "You win!"

    if message:
        result(my_cards, pc_cards)
        print(message)
        return True  
        
    return False  

while game:
    my_cards = []
    pc_cards = []

    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if play_game != 'y':
        print("Thanks for playing!")
        game = False
        break

    new_cards(my_cards, 2)
    new_cards(pc_cards, 2)

    game_over = False

    while not game_over:
        print(f"\nYour cards: {my_cards}, current score: {sum(my_cards)}")
        print(f"Computer's first card: {pc_cards[0]}")

        if check_winner(my_cards, pc_cards):
            game_over = True
            break

        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if another_card == 'y':
            new_cards(my_cards, 1)
        else:
            while sum(pc_cards) < 17:
                new_cards(pc_cards, 1)

            check_winner(my_cards, pc_cards, final=True)
            game_over = True