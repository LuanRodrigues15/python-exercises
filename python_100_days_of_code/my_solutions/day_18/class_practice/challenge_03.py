import turtle as t
import random

turtle = t.Turtle()
turtle.shape("turtle")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)

for shape_side_n in range(3, 10):
    turtle.color(random.choice(colours))
    draw_shape(shape_side_n)

