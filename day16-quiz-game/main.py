from quiz_brain import QuizBrain
from data import question_data
from question_model import Question

question_bank = []

for question in question_data:
    # question = random.choice(question_data)
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_list=question_bank)

while quiz.still_has_question():
    quiz.next_questions()

print("You completed the Quiz.")
print(f"Your final score was: {quiz.score}/{len(quiz.q_list)}")
