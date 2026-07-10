from collections import deque


class practice:
    #Print Fizz for a number multiple of 3, Buzz for multiple of 5 and FizzBuzz for multiple of both
    def fizzbuzz(self):
        for i in range(1,101):
            if i < 3:
                print(i)
            else:
                if i%3 == 0 and i%5 == 0:
                    print(i,":FizzBuzz")
                    continue
                elif i%3 == 0:
                    print(i,":Fizz")
                    continue
                elif i%5 == 0:
                    print(i,":Buzz")
    #check if a number is prime or not
    def check_prime(self,number):
        for i in range(2,int(number/2)):
            if number % i == 0:
                print("Not Prime")
                return
        print("Prime")
    #Set a password checker that outputs a welcome message when correct pwd is input
    def password_checker(self):
      self.password = "correctPassword"
      user_input = input("Input the password")

      count = 0
      while count < 10:
            if user_input == self.password:
                print("Welcome")
                return
            else:
                user_input = input("Incorrect password, Try Again!")
            count += 1
      print("Out of tries!, Cops are on the way")

    #Find the sum, average, maximum and minimum from the given list of integers
    def find_in_list(self, list_of_numbers):
        print("The average of the above list of numbers is:",sum(list_of_numbers)/len(list_of_numbers))
        print("The sum of all the numbers in the list of numbers is:",sum(list_of_numbers))
        print("The maximum number from the list of numbers is:",max(list_of_numbers))
        print("The minimum number from the list of number is:", min(list_of_numbers))

    #Create a new list from an existing list but with just unique elements
    def unique_elements_list(self,list):
        my_set = set(list)
        print(my_set)

    #Count the frequency of all the characters in a given string
    def character_counter(self,user_input):
        dict = {}
        for char in user_input:
            dict[char] = dict.get(char,0) + 1
        print(dict)

    #get the common elements from 2 lists and put it in a third list
    def find_common(self,list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        output_list = list(set1.intersection(set2))
        print(output_list)

    #pallindrome or not?
    def pallindrome(self,user_string):
        #this line means we are string from back, taking -1 steps(in reverse).
        #we can also do it like: user_string[-1::-1]
        string_reverse = user_string[::-1]
        if string_reverse == user_string:
            print("Pallindrome")
        else:
            print("Not Pallindrome")

    #Factorial calculator
    def calculate_factorial(self, num):
        result = 1
        for i in range(1,num+1):
            result *= i
        print(result)

    #This method is for practice and try outs
    def practice_method(self):
        name = "sarang"
        print(name[-1::-1])

    def valid_paranthesis(self, s: str) -> bool:
        stack = deque()
        open_set = {'(', '[', '{'}
        closed_set = {')', ']', '}'}
        for char in s:
            if char in open_set:
                stack.append(char)
            if char in closed_set:
                if len(stack) == 0:
                    return False
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                    continue

                if char == ']' and stack[-1] == '[':
                    stack.pop()
                    continue

                if char == '}' and stack[-1] == '{':
                    stack.pop()
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


obj = practice()

s = "()"
print(obj.valid_paranthesis(s))