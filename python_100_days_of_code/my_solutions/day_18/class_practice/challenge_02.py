from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.color("brown","green")

for _ in range(10):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen.exitonclick()