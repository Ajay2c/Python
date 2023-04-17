
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        question = self.question_list
        total_question = len(question)
        current_question = self.question_number
        if total_question > current_question:
            return True
        else:
            return False

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_choice = input(f"Q.{self.question_number}: {question.text}. (True/False)?: ")
        self.check_answer(user_choice, question.answer)

    def check_answer(self, user_choice, correct_answer):

        if user_choice.lower() == correct_answer.lower():
            self.score += 1
            print("you right!!")

        else:
            print("your wrong")
        print(f"the correct answer {correct_answer}")
        print(f" Your current score is: {self.score}/{self.question_number} \n")



