import colorgram
import turtle
import random

turtle.colormode(255)
tut = turtle.Turtle()
tut.speed(0)
tut.hideturtle()
tut.penup()

colors = colorgram.extract("20_001.jpg", 20)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

tut.seth(225)
tut.fd(300)
tut.seth(0)

for i in range(1, 101):
    tut.dot(20, random.choice(rgb_colors))
    tut.fd(45)
    if i % 10 == 0:
        tut.seth(90)
        tut.fd(45)
        tut.seth(180)
        tut.fd(450)
        tut.seth(0)

screen = turtle.Screen()
screen.exitonclick()
