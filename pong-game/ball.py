from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1

    def move_right(self):
        if 380 > self.xcor() > -380:
            new_x = self.xcor() + self.move_x
            new_y = self.ycor() + self.move_y
            self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_r_paddle(self):
        self.move_x = -(abs(self.move_x))
        self.move_speed *= 0.8

    def bounce_l_paddle(self):
        self.move_x = abs(self.move_x)
        self.move_speed *= 0.8

    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *= 0.8

    def start_again(self):
        self.setpos(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
