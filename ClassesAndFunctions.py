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

# the "__init__" method in any class acts as a constructor to set the initial state of an object of that class
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printData(self):
        print(self.name, self.age)

#Creating an object of the above class and calling the init method
# If a class has an init method with parameters, it is mandatory to provide arguments while creating an object of that class or we will get an exception
p1 = person("Sarang", 30)
print(p1.name)
print(p1.age)


##Inheritence in python
#This is how we inherit a parent class in a child class
class student(person):
    pass #We use the pass keyword when you do not want to add any other properties or methods to the class

s1 = student("Student", 31)
s1.printData()

#Python has a "super()" keyword to denote the parent class.
class teacher(person):
    def __init__(self,fName, lName):
        super().__init__(fName,lName)

t1 = teacher("teacher", 50)
print(t1.printData())