import random


class QuizBrain:

    def __init__(self, q_list):
        self.question_choosen=random.randint(0,len(q_list)-1)
        self.question_number=0
        self.score=0
        self.question_list= q_list

    def next_question(self):
        current_q= self.question_list[self.question_choosen]
        self.question_number+=1
        ans= input(f"Q.{self.question_number} {current_q.text} True or False? ")
        if(ans== current_q.answer):
            print(f"You got it right!\nThe correct answer is {current_q.answer}")
            self.score+=1
            print(f"Your score is {self.score}/{self.question_number}")
            return True
        else:
            print("Wrong answer")
            print(f"Your score is {self.score}/{self.question_number}")
            return False