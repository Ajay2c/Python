from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# 2) passing the question and answer in this list
question_bank = []

# 3) iterate the question  and answer by using for loop
for q_text in question_data:
    Q1 = q_text["question"]
    A1 = q_text["correct_answer"]
    f_text = Question(Q1,A1)
    question_bank.append(f_text)

#print(question_bank)

# 5) passing the question bank to the QuizBrain class
q_brain = QuizBrain(question_bank)
# 6) calling the question and next question method from QuizBrain class
while q_brain.still_has_question():
    q_brain.next_question()

# 7) final output
print("You've completed the quiz!")
q_brain.final_score()