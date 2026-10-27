class atm:
    def __init__(self, bank, branch, location, balance=1000):
        self.bank = bank
        self.branch = branch
        self.location = location
        self.balance = balance
        self.transactions = []
    def credit(self):
        amount = int(input("Enter amount to credit: "))
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Credited: {amount}")
            print("Amount credited successfully")
            print(f"Current balance:{self.balance}")
        else:
            print("Enter a valid amount")
    def debit(self):
        amount = int(input("Enter amount to debit:"))
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Debited: {amount}")
            print("Amount debited successfully")
            print(f"Current balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount")
class atm2(atm):
    def check_balance(self):
        print(f"Current balance:{self.balance}")
    def ministatement(self):
        print("Mini Statement")
        for transaction in self.transactions:
            print(transaction)
sbi = atm2("SBIN","Tadepalligudem","Railway")
while True:
    print("\nATM Menu:")
    print("1.Credit")
    print("2.Debit")
    print("3.Check Balance")
    print("4.Mini Statement")
    print("5.Exit")
    choice=input("Enter choice: ")
    if choice=="1":
        sbi.credit()
    elif choice == "2":
        sbi.debit()
    elif choice == "3":
        sbi.check_balance()
    elif choice == "4":
        sbi.ministatement()
    elif choice == "5":
        print("Thank you")
        break
    else:
        print("Invalid choice")
