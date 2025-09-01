#functions in python are defined by "def" keyword
def printQuestions(num1, num2, op):
    print("\nWhat is the solution for",num1,op,num2,"?")

def printFeedback(userAnswer, correctAnswer):
    print("Your answer is",userAnswer)
    print("Correct answer is",correctAnswer)

num1 = 10
num2 = 20

printQuestions(num1,num2,"+")
userAnswer = input("Enter you answer:\n")
correctAnswer = num1 + num2
printFeedback(userAnswer,correctAnswer)

printQuestions(num1,num2,"-")
userAnswer = input("Enter you answer:\n")
correctAnswer = num1 - num2
printFeedback(userAnswer,correctAnswer)