from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Who will win? Enter a color:")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
positions = [-150, -100, -50, 0, 50, 100, 150]
turtles = []
if user_bet:
    is_race_over = False

for i in range(7):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].penup()
    turtles[i].color(colors[i])
    turtles[i].goto(x=-230, y=positions[i])

while not is_race_over:
    for turtle in turtles:
        if turtle.xcor() > 220:
            is_race_over = True
            if user_bet == turtle.pencolor():
                print(f"You won the bet. {turtle.pencolor()} turtle won the race")
                break
            print(f"You lost the bet. {turtle.pencolor()} turtle won the race")
            break
        turtle.fd(random.randint(1, 10))

screen.exitonclick()
