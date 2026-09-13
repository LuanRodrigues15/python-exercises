from turtle import Turtle, Screen
import random as rd

screen = Screen()
turtle = Turtle()

turtle.shape("turtle")
turtle.pensize(2)
turtle.speed(70)

def RGB():
    R, G, B = tuple(((rd.randint(0, 255)) / 255) for _ in range(3)) 
    return R, G, B

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        turtle.pencolor(RGB())
        turtle.circle(200)
        turtle.setheading(turtle.heading() + size_of_gap)

draw_spirograph(5)

screen.exitonclick()