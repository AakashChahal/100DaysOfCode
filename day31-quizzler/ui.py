from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.total_questions = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text=f"{self.quiz.next_question()}",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        correct = PhotoImage(file=".\images\\true.png")
        self.true_btn = Button(image=correct, highlightthickness=0, command=self.check_true)
        self.true_btn.grid(column=0, row=2)
        wrong = PhotoImage(file=".\images\\false.png")
        self.false_btn = Button(image=wrong, highlightthickness=0, command=self.check_false)
        self.false_btn.grid(column=1, row=2)

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.total_questions + 1 == 10:
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            self.canvas.itemconfig(self.question, text=f"Quiz Over\nYour Final Score: {self.score}/10")
        else:
            self.total_questions += 1
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question)

    def check_true(self):
        self.get_solution("true")

    def check_false(self):
        self.get_solution("false")

    def get_solution(self, answer: str):
        ans = self.quiz.check_answer(answer)
        if ans:
            self.score += 1
            self.canvas.config(bg="green")
            # print("correct answer")
        else:
            self.canvas.config(bg="red")
            # print("wrong answer")
        self.feedback()

    def feedback(self):
        self.score_label.config(text=f"Score: {self.score}")
        self.window.after(1000, self.get_question)
