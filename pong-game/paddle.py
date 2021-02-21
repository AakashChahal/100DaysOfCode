from turtle import Turtle
positions_left = [(-350, 0), (-350, 20), (-350, -20)]
positions_right = [(350, 0), (350, 20), (350, -20)]
dist = 20


class Paddle(Turtle):
    def __init__(self, coord):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_len=1, stretch_wid=5)  # because the original size is 20, 20
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(coord)

    def move_up(self):
        new_y = self.ycor() + 30
        if new_y <= 250 and self.xcor() == 350:
            self.goto(350, new_y)
        elif new_y <= 250 and self.xcor() == -350:
            self.goto(-350, new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        if new_y >= -250 and self.xcor() == 350:
            self.goto(350, new_y)
        elif new_y >= -250 and self.xcor() == -350:
            self.goto(-350, new_y)
