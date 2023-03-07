#중위표기법 -> 후위표기법 변환

import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input()) #계산식의 길이
    cm = input()
    stack1, stack2 = [], []
    lst = []

    #후위 표기식으로 변환
    for i in cm:
        if i.isdigit(): #피연산자
            lst.append(i)
        else: #연산자
            if len(stack1) <= 1:
                stack1.append(i)
            else:
                lst.append(i)
    back = "".join(lst + stack1[::-1])

    #계산식
    for j in back:
        if j.isdigit():
            stack2.append(int(j))
        else:
            b = stack2.pop()
            a = stack2.pop()
            stack2.append(a+b)
    print(f'#{tc}', *stack2)