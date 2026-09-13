from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.color("brown","green")

for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

screen.exitonclick()