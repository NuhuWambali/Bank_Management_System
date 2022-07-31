# this program is written by nuhu wambali || whatsapp number +255688349680
# bankManagementSystem will allow user to do the following operations
# +deposit
# +withdraw
# +check balance

#parent class that have all user details
class User:
    def __init__(self):
          self.name = input("what is your name? ")
          self.gender = input("what is your gender? ")
          self.age = int(input("what is your age? "))

    def UserDetails(self):
        print(f"""
            User Details
            -------------
            Name : {self.name}
            Gender : {self.gender}
            Age   : {self.age}
        """)

#child class that inherit all properties of the parent class
class Bank(User):
    def __init__(self):
        self.balance = 0
     #welcome method that display a welcome and options
    def welcome(choice):
        print("""
           ***************************************************
           *                                                 *
           *          WELCOME TO ONLINE BANKING              *
           *                                                 *
           *          Choose an option below :               *
           *          1.Deposit                              *
           *          2.Withdraw                             *
           *          3.Check balance                        *
           ***************************************************
        """)
        try:
            choice = int(input("enter your choice "))
        except ValueError:
            print(" not a number")
        if choice == 1:
            show.deposit()
        elif choice == 2:
            show.withdraw()
        elif choice == 3:
            show.ViewBalance()
        else:
            print("incorrect input! try again")


    #withdraw method handle bank withdraw for 1 choice
    def deposit(self):
        self.amount = int(input("enter amount you want to deposit "))
        self.balance = self.balance + self.amount
        print(f"Account has been updated! succesfully deposit { self.amount }  new balance is { self.balance}")
        while True:
            again = input("deposite again? Y|n ")
            if again == "Y":
                show.deposit()
            else:
                exit(show.welcome())


    #withdraw method that handle bank money withdraw for 2 choice
    def withdraw(self):
        self.amount = int(input("enter the amount you want to withdraw "))
        if self.amount > self.balance:
            print(f"insufficient balance! amount available is {self.balance}")
        else:
            self.balance = self.balance - self.amount
            print(f"successfully withdraw {self.amount} amount available is {self.balance}")
        while True:
            again = input("withdraw  again? Y|n ")
            if again == "Y":
                show.withdraw()
            else:
                exit(show.welcome())
    #method that handle show details of the bank user
    def ViewBalance(self):
        print(f"your available balance is {self.balance}")
        while True:
            again = input("Check balance again? Y|n ")
            if again == "Y":
                show.ViewBalance()
            else:
                exit(show.welcome())

show1 = User()
show = Bank()
show1.UserDetails()
show.welcome()








