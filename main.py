from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()

s.setup(width=800, height=600)
s.bgcolor("black")
s.title("The Pong Game")
s.tracer(0)
rp = Paddle(350, 0)
lp = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

s.listen()
s.onkey(key="Up", fun=rp.go_up)
s.onkey(key="Down", fun=rp.go_down)
s.onkey(key="w", fun=lp.go_up)
s.onkey(key="s", fun=lp.go_down)

game_on = True
x = 0.1
while game_on:
    time.sleep(x)
    ball.move()
    s.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(rp.t) < 50 and ball.xcor() > 320 or ball.distance(lp.t) < 50 and ball.xcor() < -320:
        ball.collide()
        x *= 0.9

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        x = 0.1

    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        x = 0.1

s.exitonclick()