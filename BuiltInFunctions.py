from random import randint

a = 30.233353
b = 4
str = "   sarang   "
#round function rounds of to the nearest whole number
print(round(a))

#pow() function takes 2 inputs as the number and it's power
print(pow(b,3))

#ranint(a,b) function outputs a random integer between the given range
print(randint(10,100))

#range() function to run a loop in a given range
for i in range(1,100):
    print(i)

#To remove front and last whitespaces in the string.
print(str.strip())
#To convert a string to upper and lower case
print(str.upper())
print(str.lower())
#splitting a String at a particular character
str2 = str.split('s')
print(str2)
#Fetch a particular substring after the split
print(str2[1])
#We can concatenate multiple strings
greeting = "Hi"
name = "Sarang"
print(greeting + name)
#we can print a string in repetitive order as below
print(greeting * 2)
#We can also print the string in a formatted manner as below
print(f"{greeting} my name is {name}")
#printing the ASCII value of a character
print(ord('S'))
#Using an iterator to fetch the values from a dataset
tuple = ("Apple", "Banana", "Orange")
it = iter(tuple)
print(next(it))
