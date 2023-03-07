class Person:
    def __init__(self):
        self._age = 0
    
    @property    
    def age(self): #getter (get_age였던 함수)
        print('getter 호출!')
        return self._age
    
    @age.setter
    def age(self, age): #setter (set_age였던 함수)
        print('setter 호출!')
        self._age = age
    

    # age = property(get_age, set_age) #public -> 대신 데코레이터를 써보자

      
p1 = Person()
p1.age = 25
print(p1.age)

#p1._age = 25 #이거 안됨
#print(p1._age) # 이거 안됨

#불평편행
# p1.set_age(25)
# print(p1.get_age())