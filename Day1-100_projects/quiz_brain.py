class QuizBrain:
    def __init__(self,q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0
        
    def still_has_questions(self):
        return True if self.question_num < len(self.question_list) else False
        
    def next_question(self):
        self.current_ques  = self.question_list[self.question_num]
        self.question_num += 1
        self.get_ans = input(f"{self.question_num}: {self.current_ques.text}. (True/False)?: ")
        self.check_answer(self.get_ans,self.current_ques.answer)    
    
    def check_answer(self,user_ans,crt_ans):
        if user_ans.lower() == crt_ans.lower():
            print("you got it right...!")
            self.score += 1
        else:
            print("oops.. That's wrong")
        print(f"The correct answer is : {crt_ans}")
        print(f"Your current score is :{self.score}/{self.question_num}\n") 
        