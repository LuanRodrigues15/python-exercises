from turtle import Turtle, Screen
import random as rd

screen = Screen()
turtle = Turtle()

turtle.shape("turtle")
turtle.pensize(10)
turtle.speed(10)

direction = [0, 90, 180, 270]

def RGB():
    R, G, B = tuple(((rd.randint(0, 255)) / 255) for _ in range(3)) 
    return R, G, B

for i in range(500):
    turtle.pencolor(RGB())
    turtle.forward(100)
    turtle.setheading(rd.choice(direction))

screen.exitonclick()