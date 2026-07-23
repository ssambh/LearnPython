from selenium.webdriver.support.expected_conditions import none_of


class BankAccount:
    customer_name = None
    balance = None
    user_input = None
    def __init__(self, customer_name, balance):
        self.customer_name = customer_name
        self.balance = int(balance)

        while self.user_input != '4':
            print("Hi " + customer_name + " Welcome to the Hello World Bank. Choose from below options:")
            user_input = input(
                "Press 1. for Deposit" + "\nPress 2. for withdrawal" + "\nPress 3. for checking the balance" + "\nPress 4. to exit\n")

            if user_input == '1':
                deposit_amount = int(input("Input the amount to deposit:"))
                self.deposit(deposit_amount)

            elif user_input == '2':
                withdrawal_amount = int(input("How much do you want to withdraw?:"))
                self.withdraw(withdrawal_amount)

            elif user_input == '3':
                self.print_details()

            elif user_input == '4':
                print("Bye Bye! See you again!")
                return

            else:
                print("Incorrect Input, try again")

    def deposit(self,deposit_amount):
        self.balance += deposit_amount
        print("Your new balance is:", self.balance)

    def withdraw(self,withdrawal_amount):
        if withdrawal_amount > self.balance:
            print("Insufficient Balance!\n")
            return
        else:
            self.balance -= withdrawal_amount
        print("Cash output:", withdrawal_amount)
        print("Remaining balance", self.balance,"\n")

    def print_details(self):
        print("Customer Name:",self.customer_name)
        print("Customer Balance:", self.balance, "\n")


obj = BankAccount("Sarang", 100)