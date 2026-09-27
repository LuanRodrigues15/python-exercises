from turtle import Turtle


FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.create_text()
        self.update_score()

    def create_text(self):
        self.hideturtle()
        self.penup()
        self.color("black")
        
    def update_score(self):
        self.goto(-280, 260)
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align="center", font=FONT)