from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        with open("python-exercises/python_100_days_of_code/my_solutions/day_20_21/data.txt") as data:
             self.highscore = int(data.read())
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}\tHigh Score:{self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
            self.score += 1
            self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("python-exercises/python_100_days_of_code/my_solutions/day_20_21/data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()