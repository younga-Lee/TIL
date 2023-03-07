'''
스택을 이용해 괄호가 정상적으로 표기되어 있는지 검사하는 알고리즘

일단 ( 인 괄호가 있다면 stack에  push를 해준다, 그 후 )인 괄호가 있다면 stack에서 pop해준다
이때, stack에서 pop을 할 수 있고 (스택에 남은 괄호가 있거나), 모든 시행 결과가 스택이 [] 이라면 괄호가 정상적으로 표시되어 있다고 말할 수 있다.

이를 알고리즘으로 표현해보자면
'''
string = 'if ( ( i == 0 ) && ( j == 0)))'
def check(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        if s == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return True

'''
['(', '('] # 여는 괄호를 만나 push
['('] # 닫는 괄호를 만나 pop
[] # 닫는 괄호를 만나 pop
# 닫는 괄호를 만나 pop해야하지만 스택이 []이기 때문에 오류.

마지막 괄호가 오류이다. 왜냐하면 '('과 ')' 쌍에 맞추어서 
'''