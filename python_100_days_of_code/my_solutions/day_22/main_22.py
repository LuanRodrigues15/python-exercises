from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

for key, value in r_paddle.arrows.items():
    screen.onkeypress(lambda v=value: r_paddle.move(v), key)

for key, value in l_paddle.keyboard.items():
    screen.onkeypress(lambda v=value: l_paddle.move(v), key)

screen.listen()

game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    #Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 400:
        time.sleep(0.5)
        ball.reset_position()
        scoreboard.increase_score("r")

    #Detect L paddle misses
    if ball.xcor() < -400:
        time.sleep(0.5)
        ball.reset_position()
        scoreboard.increase_score("l")
    
screen.exitonclick()


