# i. __init__(): 인스턴스가 생성될 때 빈 리스트를 각 인스턴스의 이름 공간에 넣는다.      
# ii.empty(): 스택이 비었다면 True을 반환하고, 그렇지 않다면 False를 반환한다.
# iii.top(): 스택의 가장 마지막 데이터를 반환한다. 스택이 비었다면 None을 반환한다.
# iv.pop(): 스택의 가장 마지막 데이터의 값을 반환하고, 해당 데이터를 삭제한다.
# 스택이 비었다면 None을 반환한다.       
# v.push(): 스택의 가장 마지막 데이터 뒤에 값을 추가한다. 반환값은 없다.
# vi.__repr__: 현재 스택의 요소들을 보여준다.

class stack:
    def __init__(self, l):
        self.l = l
    
    def empty(self):
        return self.l == []
    
    def top(self):
        if self.empty() == True : return None
        return self.l[-1]
    
    def pop(self): 
        if self.empty() == True : return None
        a = self.l[-1] 
        self.l = self.l[:-1]
        return a
              
    def push(self, n):
        self.l.append(n)
        
    def __repr__(self):
        return self.l
        
s = stack([1,2,5,2,3])
print(s.empty())
print(s.top())
print(s.pop())
print(s.push(8))
print(s.__repr__())