from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scorecard import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

paddle1 = Paddle((-350, 0))  # left paddle
paddle2 = Paddle((350, 0))  # right paddle
ball = Ball()
score = Score()

screen.listen()
screen.onkey(paddle1.move_up, "w")
screen.onkey(paddle1.move_down, "s")
screen.onkey(paddle2.move_up, "Up")
screen.onkey(paddle2.move_down, "Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_right()
    # detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(paddle2) < 50 and ball.xcor() >= 330:
        ball.bounce_r_paddle()

    elif ball.distance(paddle1) < 50 and ball.xcor() <= -330:
        ball.bounce_l_paddle()

    if ball.xcor() >= 380:
        ball.start_again()
        score.player1_score()

    elif ball.xcor() <= -380:
        ball.start_again()
        score.player2_score()

screen.exitonclick()
