import turtle
from turtle import Turtle
import random
CAR_DISTANCE = list(range(-200, 210))
turtle.register_shape("car.gif")
turtle.register_shape("car2.gif")
turtle.register_shape("car3.gif")
turtle.register_shape("car4.gif")
SHAPE = ["car.gif", "car2.gif", "car3.gif", "car4.gif"]


class Car:
    """class Car is used to create cars at random location on the screen and move them from right to left direction on
    the screen"""
    def __init__(self):
        self.cars = []
        self.generate_new_car()

    def generate_new_car(self):
        if random.randint(1, 6) == 1:
            r, g, b = random.random(), random.random(), random.random()
            new_car = Turtle(shape=random.choice(SHAPE))
            new_car.color(r, g, b)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.seth(180)
            new_car.goto(415, random.choice(CAR_DISTANCE))
            self.cars.append(new_car)

    def move_cars(self, level):
        for car in self.cars:
            car.speed(10 / level)
            car.fd(10)
