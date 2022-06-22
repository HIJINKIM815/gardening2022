# 새로운 클래스 정의 

class Man: # 클래스의 이름 : Man
    def __init__(self, name): # 메서드 중 __init__ 라는 클래스를 초기화하는 방법을 정의
        self.name = name
        print("Initialized!")
        
    def hello(self): # 메서드 1
        print("Hello " + self.name + "!")
        
    def goodbye(self): # 메서드 2
        print("Good-bye " + self.name + "!")

m = Man("David")
m.hello()
m.goodbye()