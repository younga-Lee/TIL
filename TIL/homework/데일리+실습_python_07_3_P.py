class Calculator:
    
    def __init__(self):
        pass
    
    def cal(self, formula):
        f = formula.split()
        if f[1] == '+':
            result =  int(f[0])+int(f[2])
        elif f[1] == '-':
            result =  int(f[0])-int(f[2])
        elif f[1] == '*':
            result =  int(f[0])*int(f[2])
        elif f[1] == '/':    
            try :
                result =  int(f[0])/int(f[2])
            except ZeroDivisionError:
                result = '0으로 나눌 수 없습니다'
        return result
                
c = Calculator()   
print(c.cal('4 / 0'))       
    

# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0