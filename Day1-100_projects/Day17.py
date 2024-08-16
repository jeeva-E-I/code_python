from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
i =0
question_bank = []

for key1,key2 in question_data:
    new_q = Question(question_data[i][key1],question_data[i][key2])
    question_bank.append(new_q)
    i +=1

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is :{quiz.score}/{quiz.question_num}\n") 
# print(question_bank[0].text) {"Accesing the list in dictionaries"}
# print(question_bank[0].answer)