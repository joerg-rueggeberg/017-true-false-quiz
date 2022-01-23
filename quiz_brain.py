class QuizBrain:
    def __init__(self, get_question_list):
        self.question_list = get_question_list
        self.question_number = 0
        self.score = 0

    # TODO 3: Check if end of Quiz
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # TODO 1: Ask Questions
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Question {self.question_number}/{len(self.question_list)}: "
                            f"{question.text} (True/False)?: ")
        # Sendet user_answer und question.answer zur Weiterverarbeitung an check_answer
        self.check_answer(user_answer, question.answer)

    # TODO 2: Check if correct
    # Empfängt user_answer und question.answer auf next_question
    def check_answer(self, get_user_answer, get_question_answer):
        if get_user_answer.lower() == get_question_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {get_question_answer}.")
        if self.question_number != 12:
            print(f"Your current score is: {self.score}/{self.question_number}.")
        print()
