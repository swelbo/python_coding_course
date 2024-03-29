class QuizBrain:
    ''' Function that manages the quiz brain '''
    def __init__(self, question_list) -> None:
        
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def questions_remaining(self):
        return self.question_number != len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_input, current_question.answer)
    
    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1 
        else:
            print("Wrong!")
        
        print(f"The correct answer was: {correct_answer}. ")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
