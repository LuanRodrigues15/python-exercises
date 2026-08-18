print(r'''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/_____/____/____/__/[LuanRodrigues15]
******************************************************************************* ''')

print('Welcome to Treasure Island\nYour mission is to find the treasure.')
startGame = False

questionStart = input("Do you want to start the game? S/N: ")
if questionStart.upper() == "S":
    startGame = True
else:
    print("Okay, see you later!")

while startGame:
    print("Choice your path... Good Luck!")

    print("You're at a crossrod, where do you want to go?")
    if input("Left or Right? L/R: ") == "L":
        print("There is an insland in the middle of the lake. You can wait for a boat or swim...")
        if input("Swim or Wait? S/W: ") == "W":
            print("You arrive at the island unharmed. There is house with 3 door. One red, one yellow and one blue.")
            door = input("Which door?\nYELLOW\nBLUE\nRED\n(Y, B or R): ")
            if  door == "Y":
                print("You found the treasure. You Win! XD")
            elif door == "R":
                print("Burned by fire.\nGame Over.")
            elif door == "B":
                print("Eaten by beasts.\nGame Over.")
            else: 
                print("Game Over.")
        else: 
            print("Attacked by trout.\nGame Over.") 
    else:
        print("Fall into a hole.\nGame Over.")

    questionStart = input("Do you want to restart the game? S/N: ")
    
    if questionStart.upper() == "N":
        startGame = False
        print("Thanks! :)")
    else: 
        print("Try again! Good Luck!")
        startGame = True