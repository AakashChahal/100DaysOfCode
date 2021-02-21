from turtle import Turtle
import time


class Score(Turtle):
    """Score class is used to manage the score and level of the user."""
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.ht()
        if self.level == 1:
            self.print_level()

    def print_level(self):
        self.clear()
        self.setpos(-330, 220)
        self.write(f"LEVEL: {self.level}", move=False, align="center", font=("Courier", 14, "bold"))

    def next_level(self):
        self.level += 1
        self.clear()
        self.setpos(0, 0)
        self.write(f"LEVEL UP", move=False, align="center", font=("Courier", 14, "bold"))
        time.sleep(1)
        self.print_level()

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"Game Over", move=False, align="center", font=("Courier", 14, "bold"))
        self.setpos(0, -20)
        self.write(f"You got hit by a car at level {self.level}",
                   move=False, align="center", font=("Courier", 14, "bold"))
