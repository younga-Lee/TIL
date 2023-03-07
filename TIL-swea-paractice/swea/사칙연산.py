import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    lst = [0]*(N+1)

    for i in range(N-1, -1, -1):
        if len(arr[i]) == 2:
            a, b = map(int, arr[i])
            lst[a] = b
        else: #연산이 들어 있을 경우
            a, b, c, d = arr[i]
            a, c, d = int(a), int(c), int(d)
            if b == '-':
                lst[a] = lst[c] - lst[d]
            if b == '+':
                lst[a] = lst[c] + lst[d]
            if b == '/':
                lst[a] = lst[c] / lst[d]
            if b == '*':
                lst[a] = lst[c] * lst[d]

    print(f'#{tc}', int(lst[1]))


