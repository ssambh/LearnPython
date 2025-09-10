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


obj = practice()
list_of_numbers = [1,2,3,4,5]
obj.find_in_list(list_of_numbers)