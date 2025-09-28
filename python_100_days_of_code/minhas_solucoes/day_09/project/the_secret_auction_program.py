import os

print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________
                         `'-------'`
                       .-------------.
                      /_______________\\
      ''')
print("Welcome to the secrect auction program.")

bidders = {}
continue_bidding = True

while continue_bidding:
    name = input("What's your name? ")
    price = float(input("What's your bid? $"))

    bidders[name] = price
    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if answer == "no":
        continue_bidding = False
    else:
        os.system("cls")
        continue

winner = ""
highestBid = 0.0

for key in bidders:
    if bidders[key] > highestBid:
        highestBid = bidders[key]
        winner = key

os.system("cls")

print(f"The winner is {name} with a bid of ${highestBid}")
# Another option (wouldn't need 'For')
# print(f"The winner is {max(bidders, key=bidders.get)} with a bid of ${bidders[max(bidders, key=bidders.get)]}")