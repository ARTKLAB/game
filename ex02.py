class Account:
    def __init__(self, accountNo, ownerName, Balance) :
        self.sccountNo = accountNo
        self.ownerName = ownerName
        self.Balance = Balance
    # 입금한다
    def deposit(self, amount):
        self.Balance += amount #150,000
        
    # 출금한다
    def withdraw(self, amount):
        if self.Balance < amount :
            return 0
        self.Balance -= amount
        return amount
            
obj1 = Account("111-222-33333333", "정수아", 50000)
obj2 = Account("555-666-77777777", "손이안", 100000)

# 10만원 입금
obj1.deposit(100000)
# 3만월 출금
obj2.withdraw(30000)


def printAccount(obj):
    print("계좌번호:" + obj.accountNo)
    print("예금주 이름:" + obj.ownerName)
    print(" 잔액:" + str(obj.Balance))
    print()
    

printAccount(obj1)
printAccount(obj2)
