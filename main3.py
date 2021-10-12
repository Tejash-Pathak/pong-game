from ball import *
from paddle import *
from scoreboard import *
import time
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title(
    "                                                                                                                        Pong")
screen.tracer(0)
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() >= 320:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() >= -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()
screen.exitonclick()
