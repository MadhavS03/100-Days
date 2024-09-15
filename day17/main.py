### Creating our own Class ###
### pass -> passes code to the next line without doing anything ###

# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow (self, user):
#         user.followers += 1
#         self.following += 1
#
# user = User()
# user_1 = User('01', 'Madhav')
# user_2 = User('03', 'Sharma')
#
# print(user_1.username)
# user_1.follow(user_2)
# print(user_2.followers)


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    new_question = Question(i['text'], i['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Quiz completed!")
print(f"Final score: {quiz.score}/12")
