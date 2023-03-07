# #문제
# 개의 속성과 행위를 정의하는 Doggy 클래스를 만들어라. 

# 초기화 메서드는 인자로 개의 이름과 견종을 받아서 인스턴스 변수에 할당한다.
# bark() 메서드를 호출하면 개는 짖을 수 있다
# 클래스 변수는 태어난 개의 숫자와 현재 있는 개의 숫자를 기록하는 변수로 구성한다.
# 개가 태어나면 num_of_dogs와 birth_of_dogs의 값이 각 1씩 증가한다.
# 개가 죽으면 num_of_dogs의 값이 1 감소한다.
# get_status() 메서드를 호출하면 birth_of_dogs와 num_of_dogs의 수를 출력할 수 있다 

class Doggy:
    num_of_dogs = 0  #클래스 변수
    birth_of_dogs = 0
    
    def __init__(self, name, dogtype):
        self.name = name
        self.dogtype = dogtype
        
    def bark(self):
        return print('왈왈')

    def get_status(self):
        return self.birth_of_dogs, self.num_of_dogs
        
    def birth(self):
        self.num_of_dogs += 1
        self.birth_of_dogs += 1
    
    def deth(self):
        self.num_of_dogs -= 1
        
