from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from game_art import logo
import os

question_bank = []
for question_index in question_data:
    question = Question(question=question_index["question"], answer=question_index["correct_answer"])
    question_bank.append(question)

quiz_brain = QuizBrain(question_list=question_bank)


while quiz_brain.still_has_question_remaining():
    if quiz_brain.get_question_index() % 2 == 0:
        if quiz_brain.get_question_index() != 0:
            os.system("pause")
        os.system("cls")
        print(logo)
    quiz_brain.next_question()
quiz_brain.quiz_completed()
