from turtle import Turtle


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setpos(0, 270)
        self.ht()
        self.write(f"SCORE: {self.score}", move=False, align="center", font=("Courier", 14, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", move=False, align="center", font=("Courier", 14, "bold"))
        
    def game_over(self):
        self.clear()
        self.setpos(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Courier", 14, "bold"))
        self.setpos(0, -20)
        self.write(f"Final Score: {self.score}", move=False, align="center", font=("Courier", 14, "bold"))
