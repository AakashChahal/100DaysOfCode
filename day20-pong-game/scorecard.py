from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.ht()
        self.update_score()

    def update_score(self):
        self.goto(-300, 250)
        self.write(f"Player1 = {self.l_score}", align="left", font=("Courier", 14, "bold"))
        self.goto(150, 250)
        self.write(f"Player2 = {self.r_score}", align="left", font=("Courier", 14, "bold"))

    def player1_score(self):
        self.clear()
        self.l_score += 1
        self.update_score()

    def player2_score(self):
        self.clear()
        self.r_score += 1
        self.update_score()
