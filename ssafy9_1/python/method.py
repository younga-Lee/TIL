class MyClass:
    
    def method(self):
        return '인스턴스 메서드'
    
    @classmethod
    def classmethod(cls):
        return '클래스 메서드'
    
    @staticmethod
    def staticmethod():
        return '스태틱 메서드'
    
my_class = MyClass()
print(my_class.method()) #모두다 접근 가능
print(my_class.classmethod()) #클래스, static만 접근 가능
print(my_class.staticmethod())