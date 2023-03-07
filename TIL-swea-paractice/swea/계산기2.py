import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    cm = input()
    stack = []
    lst = []
    pri = {'+': 1, '*': 2}

    #후위표기법
    for c in cm:
        if c.isdigit():
            lst.append(c)
        else:
            while stack and pri[stack[-1]] >= pri[c]:
                lst.append(stack.pop())
            stack.append(c)

    lst = lst + stack[::-1]


    #계산
    cal = []
    for i in lst:
        if i.isdigit():
            cal.append(int(i))
        elif len(cal) >= 2:
            a2 = cal.pop()
            a1 = cal.pop()
            if i == '+':
                cal.append(a1+a2)
            if i == '*':
                cal.append(a1*a2)

    print(f'#{tc}', *cal)