import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    word = input()
    stack = []

    for i in word:
        if i not in stack: #스택에 없으면 값추가
            stack.append(i)
        elif stack != []: #스택이 0이 아니라면 pop()
            a = stack.pop()
            if i == a: #pop한 값이 그 전 값과 같다면 = 연속된 값이라면 제거
                pass
            else:
                stack.append(a) #연속되지않았다면 pop한 것을 다시 원상복구
                stack.append(i) #i를 stack에 쌓기 -> 이거 중요!

    print(f'#{tc}', len(stack))

