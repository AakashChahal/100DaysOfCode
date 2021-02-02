from turtle import Turtle


class Player(Turtle):
    """Player class is used to create, move and manage the turtle on screen."""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.setpos(0, -230)
        
    def move_up(self):
        if self.ycor() <= 220:
            self.goto(self.xcor(), self.ycor() + 10)

    def move_down(self):
        if self.ycor() >= -220:
            self.goto(self.xcor(), self.ycor() - 10)
            
    def next_level(self):
        self.setpos(0, -230)
