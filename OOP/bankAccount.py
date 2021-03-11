class Account():
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print(f"Added {deposit_amount} to the balacnce")

    def withdrawal(self,withdrawal_amount):
        if self.balance >= withdrawal_amount:
            self.balance = self.balance - withdrawal_amount
            print("Withdrawal accepted")
        else:
            print("Sorry not enough funds!")

    def __str__(self):
        return f"Owner is: {self.owner} \n Balance is: {self.balance}"


a = Account("Sam",500)
print(a.balance)
print(a.owner)
print(a)

a.deposit(100)

a.withdrawal(600)
a.withdrawal(50)