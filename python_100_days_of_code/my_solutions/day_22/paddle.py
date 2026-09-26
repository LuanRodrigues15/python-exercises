from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.arrows = {"Up":90, "Down":270}
        self.keyboard = {"w":90, "s":270}
        self.create_paddles()
        self.goto(position)


    def create_paddles(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def move(self, direction):
        if direction == 90:
            new_y = self.ycor() + MOVE_DISTANCE
        else:
            new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)