class Account:
    def __init__(self, accountNo, ownerName, balance):
        self.accountNo = accountNo
        self.ownerName = ownerName
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def printAccount(self):
        print(f"계좌번호 : {self.accountNo}")
        print(f"예금주 이름 : {self.ownerName}")
        print(f"잔액 : {self.balance}")

obj1 = Account("111-222-33333333", "박재현", 50000)
obj2 = Account("555-666-77777777", "손이안", 100000)

obj1.deposit(100000)
obj2.withdraw(30000)

obj1.printAccount()
print()
obj2.printAccount()
print()
