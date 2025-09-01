import random

a = 10
b = 20
#Addition operator
print(a + b)
#Subtraction operator
print(a - b)
#Multiplication Operator
print(a * b)
#Division operator.
#'/' of 2 number(integer/floating) results in a decimal value.
print(a/b)
#'//' of 2 integers results in an integer value without the decimal
c = 2
d = 1
print(b//a)
#If either of the operands is a floating number then the result will be a floating value.
c = 2.0
d = 1
print(c//d)
#To find the remainder
print(c%d)
#'To the power of' operator
print(a ** 2)
#Range operator to print a random number between the given range
print(random.randrange(5,15))
#Using " in a string
str = "My name is \"Sarang\""
print(str)

#Slicing: fetching a character from a string.
print(str[3])
#Slicing: fetching characters of a string from the back
print(str[-10])
#Slicing: fetching a substring from an index through the end of the list
print(str[2:])
#Fetching a substring from a string with reference from the back
print(str[-4:]) #This will print the substring starting from the 4th character from the back till the end of the string
#Reversing a string
print(str[::-1])
#Slicing: fetching a substring from a string.
print(str[0:10]) #10th character not inclusive

#-----Logical Operators-------------
a = 10
b = 20
if a and b == 10:
    print("Equal")
elif a or b == 20:
    print("One is greater")

