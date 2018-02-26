class Member:
    def __init__(self, id='', name='', point=0):
        self.__id = id
        self.__name = name
        self.__point = point

    def setId(self, id):
        self.__id = id
    
    def getId(self):
        return self.__id
    
    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name
    
    def setPoint(self, point):
        self.__point = point
    
    def getPoint(self):
        return self.__point

if __name__ == '__main__':
    member = Member()
    member.setId('thanatos0128')
    member.setName('박정제')
    member.setPoint(10000)

    print(member.getId(), member.getName(), member.getPoint(), sep=' : ')