print('### Welcome to The Python Quiz ###')
answer = input('Are you ready to play the Quiz ? (yes/no): ')
print("\n")

questions = [
    {
        "questionTitle": "What is your Favourite programming language?",
        "answer": "python"
    },
    {
        "questionTitle": "What do we use to define a block of code in Python language?",
        "answer": "indentation"
    },
    {
        "questionTitle": "What is the method inside the class in python language?",
        "answer": "function"
    }
]

def generateQuestions(questionNo, questionTitle, answer):
    user_answer = input("Question #" + str(questionNo) + ". " + questionTitle + " ")
    user_answer = user_answer.lower().strip()
    if user_answer == answer:
        print('Correct!', end="\n\n")
        return 1
    else:
        print("You're answer seems wrong :( The correct answer is " + answer, end="\n\n")
        return 0

def startGame():
    score = 0
    for q in range(len(questions)):
        score += generateQuestions(q+1, questions[q]["questionTitle"], questions[q]["answer"])
    print("Final Score: " + str(score))

startGame()