class Account():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,dep_amt):
        self.balance=self.balance + dep_amt
        print(f"added {dep_amt}")
    def withdraw(self,wd_amt):
        if wd_amt<=self.balance:
            self.balance=self.balance-wd_amt
            print("withdrawal accepted")
        else:
            print("not enough funds")
    def __str__(self):
        return f"Owner:{self.owner} \nBalance={self.balance}"
a=Account('ayush')
print(a)
a.deposit(1000)
print(a)
a.withdraw(900)