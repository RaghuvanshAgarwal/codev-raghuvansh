import random


def correct_answer_applaud():
    applaud = ["You are doing good.", "Keep it up.", "You can do this.", "Stay Strong.", "Bravo.", "You are Awesome.",
               "There you go!", "Keep up the good work.", "Good job.", "I’m so proud of you!"]
    return random.choice(applaud)


def wrong_answer_encouragement():
    encouragement = ["Hang in there.", "Don’t give up.", "Keep pushing.", "Keep fighting!", "Stay strong."
                     , "Never give up.", "Never say ‘die’.", "Come on! You can do it!."]
    return random.choice(encouragement)


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.correct_answer_count = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f" Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(user_answer=user_answer, correct_answer=question.answer)

    def still_has_question_remaining(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print(f"Correct {correct_answer_applaud()}")
            self.correct_answer_count += 1
        else:
            print(f"That's Wrong, Correct Answer Was {correct_answer}, {wrong_answer_encouragement()}")
        print(f"Your Current Score is : {self.correct_answer_count}/{self.question_number}\n")

    def get_question_index(self):
        return self.question_number

    def quiz_completed(self):
        print("You've completed the quiz")
        print(f"Your final score was: {self.correct_answer_count}/{len(self.question_list)}")
