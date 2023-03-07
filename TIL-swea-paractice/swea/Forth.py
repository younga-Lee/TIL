import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    cm = input().split()
    stack =[] #숫자넣을 stack
    ans = ''

    for i in cm:
        if i == '.':
            break
        elif i.isdigit():
            stack.append(int(i))
        else: #연산자
            if len(stack) >= 2:
                b = int(stack.pop()) #pop은 마지막 순서대로
                a = int(stack.pop())
                if i == '+':
                    stack.append(a+b)
                elif i == '*':
                    stack.append(a*b)
                elif i == '/':
                    stack.append(a//b)     #나누기할 때 float로 형태 바뀜 주의!!
                elif i == '-':
                    stack.append(a-b)
            else:
                ans = 'error'
                break
        if len(stack) == 1: ans = stack[0] #맨마지막에 숫자가 올 경우도 고려해야함
        else: ans = 'error'

    print(f'#{tc}', ans) 
