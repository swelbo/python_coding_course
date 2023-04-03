from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# for loop that will generate the question bank. 
question_bank = []
for question in question_data:
    obj = Question(text=question["question"], answer=question["correct_answer"])
    question_bank.append(obj)

quiz = QuizBrain(question_list=question_bank)

while quiz.questions_remaining():
    quiz.next_question()

print("*******************************")
print("You have completed the quiz!!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
print("*******************************")
print("\n")