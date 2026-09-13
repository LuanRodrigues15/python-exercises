from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

keys_pressed = {
    "Up": False,
    "Down": False,
    "Left": False,
    "Right": False
}

def press_up(): keys_pressed["Up"] = True
def release_up(): keys_pressed["Up"] = False

def press_down(): keys_pressed["Down"] = True
def release_down(): keys_pressed["Down"] = False

def press_left(): keys_pressed["Left"] = True
def release_left(): keys_pressed["Left"] = False

def press_right(): keys_pressed["Right"] = True
def release_right(): keys_pressed["Right"] = False

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

def move_loop():
    if keys_pressed["Up"]:
        turtle.forward(10)
    if keys_pressed["Down"]:
        turtle.backward(10)
    if keys_pressed["Left"]:
        turtle.left(10)
    if keys_pressed["Right"]:
        turtle.right(10)
        
    screen.ontimer(move_loop, 20)

screen.listen()

screen.onkeypress(press_up, "Up")
screen.onkeypress(press_down, "Down")
screen.onkeypress(press_left, "Left")
screen.onkeypress(press_right, "Right")
screen.onkeypress(clear, "c")

screen.onkeyrelease(release_up, "Up")
screen.onkeyrelease(release_down, "Down")
screen.onkeyrelease(release_left, "Left")
screen.onkeyrelease(release_right, "Right")

move_loop()

screen.exitonclick()