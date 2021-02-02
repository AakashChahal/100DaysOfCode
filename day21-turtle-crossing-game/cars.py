from turtle import Turtle
import random
import time
CAR_DISTANCE = list(range(-200, 230))


class Car:
    """class Car is used to create cars at random location on the screen and move them from right to left direction on
    the screen"""
    def __init__(self):
        self.cars = []
        self.generate_new_car()

    def generate_new_car(self):
        if random.randint(1, 6) == 1:
            r, g, b = random.random(), random.random(), random.random()
            new_car = Turtle(shape="square")
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
