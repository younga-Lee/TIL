import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    word = input()
    ans = 1
    stack = []

    for s in word:
        if s == '(' or s == '{':
            stack.append(s)
        elif s == ')':
            if len(stack) == 0:
                ans = 0
                break
            else:
                if stack.pop() == '(':
                    pass
                else:
                    ans = 0
                    break

        elif s == '}':
            if len(stack) == 0:
                ans = 0
                break
            else:
                if stack.pop() == '{':
                    pass
                else:
                    ans = 0
                    break
        else:
            pass
    if stack: ans = 0

    print(f'#{tc} {ans}')