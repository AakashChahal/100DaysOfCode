# TODO: #1 asking the questions
# TODO: #2 check if answer was correct
# TODO: #3 checking if we're at the end of the quiz

class QuizBrain:

    def __init__(self, question_list):
        self.q_num = 0
        self.q_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.q_num < len(self.q_list)

    def next_questions(self):
        user_ans = input(f"Q.{self.q_num + 1} {self.q_list[self.q_num].text}. (True/False)?: ")
        if user_ans == self.q_list[self.q_num].ans:
            self.score += 1
            print("You got it right!")
        else:
            print("You are wrong.")
        print(f"The correct answer: {self.q_list[self.q_num].ans}")
        print(f"Current score: {self.score}/{len(self.q_list)}")
        print()
        self.q_num += 1
