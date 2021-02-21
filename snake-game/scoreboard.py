import time
from turtle import Turtle
FILE = open("data.txt")
score = int(FILE.read())
FILE.close()


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = score
        self.color("white")
        self.penup()
        self.ht()
        self.update()

    def update(self):
        self.clear()
        self.setpos(0, 270)
        self.write(f"SCORE: {self.score}, High Score: {self.high_score}", move=False, align="center",
                   font=("Courier", 14, "bold"))

    def increase_score(self):
        self.score += 1
        self.update()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.clear()
        self.setpos(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Courier", 14, "bold"))
        self.setpos(0, -20)
        self.write(f"Final Score: {self.score} High Score: {self.high_score}",
                   move=False, align="center", font=("Courier", 14, "bold"))
        time.sleep(1)
        self.score = 0
        self.update()
