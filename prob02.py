class Goods:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock
        print(self)
    
    def __str__(self):
        # 문자열 포맷팅
        return '{0}(가격:{1}원)이 {2}개 입고 되었습니다.'.format(self.__name, self.__price, self.__stock)
    
    def __repr__(self):
        return '이 제품은 {0}입니다'.format(self.__name)

if __name__ == '__main__':
    input_list = []
    for i in range(3):
        input_list.append(input().split())
    
    goods_list = []
    for i in range(3):
        goods_list.append(Goods(input_list[i][0], input_list[i][1], input_list[i][2]))