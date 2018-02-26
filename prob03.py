# 클래스 메소드와 클래스 변수에 대해 알 수 있는 예제

class CurrencyConverter:
    __rate = 1000

    @classmethod
    def toDollar(cls, won):
        return won/cls.__rate

    @classmethod
    def toKRW(cls, dollar):
        return dollar*cls.__rate

    @classmethod
    def setRate(cls, r):
        # __rate = r 은 안된다. 클래스 변수는 cls키워드를 통해서
        cls.__rate = r

    # @staticmethod
    # def printRate():
    #     print(cls.__rate)

if __name__ == '__main__':
    CurrencyConverter.setRate(1121)

    print('백만원은 {}달러입니다'.format(CurrencyConverter.toDollar(1000000)))
    print('백달러는 {}원입니다.'.format(CurrencyConverter.toKRW(100)))
