from quiz_brain import QuizBrain
from question_model import Question
from data import question_data
from art import logo

question_bank = []
for i in question_data:
    question_bank.append(Question(i["question"], i["correct_answer"]))

quiz = QuizBrain(question_bank)
print(logo)
print("-----------------------------\nCategory: Science -> Computer\n-----------------------------")

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}.")
