import sys
sys.stdin = open("s_input.txt", "r")

for tc in range(1, 4):
    n, word = input().split()
    n = int(n)
    stack = []

    for i in range(n):
        if word[i] not in stack: #스택에 없으면 값추가
            stack.append(word[i])
        elif stack != []: #스택이 0이 아니라면 pop()
            a = stack.pop()
            if word[i] == a: #pop한 값이 그 전 값과 같다면 = 연속된 값이라면 제거
                pass
            else:
                stack.append(a) #연속되지않았다면 pop한 것을 다시 원상복구
                stack.append(word[i])

    print(f'#{tc}', ''.join(stack))