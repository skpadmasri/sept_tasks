# ====== OCT-12-2-2026 ======

# Task-1
# Practice using Classes and Objects by writing a program to create a Laptop object

class Laptop():
    brand = "Dell"
    color = "Black"
    model = "2024"
    def calling(self):
        print(f"Welcome to {self.brand}") 
dell = Laptop()
dell.calling()

# # Task-2

# #Implement an ATM program using OOP concepts: Class, Object, Inheritance.

class UserDetails:
    user_name = "padmasri"
    account_num = "1234567890"
    def details(self):
        print("User Name:", self.user_name)
        print("Account Number:", self.account_num)
class ATM(UserDetails):
    balance = 0
    def credit(self):
        amount = int(input("Enter amount to credit: "))
        if amount > 0:
            self.balance += amount
            print("Amount credited successfully!")
        else:
            print("Enter a valid amount")
    def debit(self):
        amount = int(input("Enter amount to debit: "))
        if amount <= 0:
            print("Enter a valid amount")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount debited successfully!")
        else:
            print("Insufficient balance")
    def check_balance(self):
        print("Available Balance:", self.balance)
atm1 = ATM()
atm1.details()
while True:
    print("\n1. Credit")
    print("2. Debit")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        atm1.credit()
    elif choice == "2":
        atm1.debit()
    elif choice == "3":
        atm1.check_balance()
    elif choice == "4":
        print("Thank you for using ATM!")
        break
    else:
        print("Invalid choice")

        
        
#======     14-10-2026     =======

#Practice using polymorphism encapsulation and implement in atm


class UserDetails:
    def __init__(self):
        self.user_name = "padmasri"
        self.account_num = "1234567890"

    def details(self):
        print("User Name:", self.user_name)
        print("Account Number:", self.account_num)

class ATM(UserDetails):
    def __init__(self):
        super().__init__()
        self.__balance = 0   # Encapsulation

    def credit(self):
        amount = int(input("Enter amount to credit: "))

        if amount > 0:
            self.__balance += amount
            print("Amount credited successfully!")
        else:
            print("Enter a valid amount")

    def debit(self):
        amount = int(input("Enter amount to debit: "))

        if amount <= 0:
            print("Enter a valid amount")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Amount debited successfully!")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Available Balance:", self.__balance)

    # Polymorphism: overriding the parent method
    def details(self):
        print("Welcome to ATM")
        super().details()
        self.check_balance()


atm1 = ATM()
atm1.details()

while True:
    print("\n1. Credit")
    print("2. Debit")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        atm1.credit()
    elif choice == "2":
        atm1.debit()
    elif choice == "3":
        atm1.check_balance()
    elif choice == "4":
        print("Thank you for using ATM!")
        break
    else:
        print("Invalid choice")

#Practice using abstraction by writing a program and sharing the file.

from abc import ABC, abstractmethod
class Abstract_demo(ABC):
    @abstractmethod
    def details(self):
        pass
    @abstractmethod
    def details2(self):
        pass
class Demo(Abstract_demo):
    def details(self):
        print("Implementation done 1")
    def details2(self):
        print("Implementation 2 done")
obj = Demo()
obj.details()
obj.details2()