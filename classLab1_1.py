class Account:
    def __init__(self, accountNo, ownerName, balance):
        self.accountNo = accountNo
        self.ownerName = ownerName
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


obj1 = Account("111-222-33333333", "박재현", 50000)
obj2 = Account("555-666-77777777", "손이안", 100000)

obj1.deposit(100000)
obj2.withdraw(30000)


def printAccount(obj):
    print(f"계좌번호 : {obj.accountNo}")
    print(f"예금주 이름 : {obj.ownerName}")
    print(f"잔액 : {obj.balance}")

printAccount(obj1)
print()
printAccount(obj2)