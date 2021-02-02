from turtle import Screen
import time
from cars import Car
from scoreboard import Score
from player import Player

screen = Screen()
screen.setup(width=800, height=500)
screen.tracer(0)

player = Player()
car = Car()
score = Score()

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() <= 220 or player.ycor() >= -220:
        car.generate_new_car()
        car.move_cars(score.level)

    if player.ycor() >= 220:
        score.next_level()
        player.next_level()

    for next_car in car.cars:
        if next_car.distance(player) < 25:
            score.game_over()
            game_is_on = False

screen.exitonclick()
