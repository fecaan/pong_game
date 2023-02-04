from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    #top yukarı ya da aşağı duvara çarpıp geri sekmesi
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    #topun sağ ve sol raketlere çarparak sekmesi
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #sağ raketin topu kaçırması
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    #sol raketin topu kaçırması
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()
