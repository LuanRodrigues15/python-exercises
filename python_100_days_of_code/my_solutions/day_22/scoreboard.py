from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 240)
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.write(arg=f"{self.l_score}\t{self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, paddle):
        if paddle == "r":
            self.l_score += 1
        else:
            self.r_score += 1
        self.clear()
        self.update_score()