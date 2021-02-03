from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True
while game_on:
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extend_snake()
        food.new_food()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.restart()

    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.restart()

screen.exitonclick()
