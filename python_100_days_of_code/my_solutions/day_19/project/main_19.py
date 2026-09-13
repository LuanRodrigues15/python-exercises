from turtle import Turtle, Screen
import random as rd

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "blue", "green", "orange", "yellow"]
turtles = []

def start_game():
    turtles.clear()

    y_positions = [-80, -40, 0, 40, 80]
    for i, color in enumerate(colors):
        t = Turtle(shape="turtle")
        t.color(color)
        t.penup()
        t.goto(x=-230, y=y_positions[i])
        turtles.append(t)

def run_race():
    start_game()
    bet = screen.textinput("Make your bet", f"Who will win? ({'/'.join(colors)}):")
    
    if not bet:
        return False
        
    is_racing = True
    while is_racing:
        for t in turtles:
            step = rd.randint(1, 10)
            t.forward(step)

            # Check if turtle crossed the finish line
            if t.xcor() >= 220:
                is_racing = False
                winner_color = t.color()[0]
                
                if winner_color.lower() == bet.lower():
                    result_msg = f"You won! The {winner_color} turtle finished first!"
                else:
                    result_msg = f"You lost! The {winner_color} turtle won."
                
                again = screen.textinput(result_msg, "Play again? (Y/N):")
                return again is not None and again.lower().strip() == "y"

play = True
while play:
    play = run_race()
    if play:
        screen.clearscreen()

screen.bye()