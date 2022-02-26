# 사용자로부터 상품코드, 재고 수량을 입력받아 상품 객체를 생성
# 상품의 수량을 추가하면 추가 된 수량을 출력
# 클래스이름 ( GoodStuck), 수량추가 (addStock)


# 클래스 선언
class GoodStock:
    def __init__(self, number, score):
        # 상품코드
        self.goodcode = num1
        # 재고수량
        self.stocknum = num2
    # 재고 수량 더하는 함수
    def addstock(self, amount):
        # 클라스가 가진 재고 수량 변수 = 기존 재고수량 + 추가 재고 수량
        # self.stockNum = self.stockNum + amount
        self.stocknum += amount
        

num1 = input(' 상품코드를 입력해주세요: ')
num2 = int(input(' 재고를 입력해 주세요: '))

obj = GoodStock(num1, num2)

amount = int(input(' 추가할 수량을 입력하세요:'))
obj.addstock(amount)
print(num1," 재고 수량 : ", obj.stocknum)
