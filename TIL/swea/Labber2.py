import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    T = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    # 출구 인덱스들 찾기
    choice = []
    for x in range(100):
        if arr[-1][x] == 1:
            choice.append(x)

    # 위로 올라가기
    mn = short = 10000
    for n in choice:
        cnt = 0
        for i in range(98, -1, -1):
            if arr[i][n - 1] == 1:
                while 0 < n - 1 <= 100 and arr[i][n - 1] == 1:
                    n = n - 1
                    cnt += 1
            elif arr[i][n + 1] == 1:
                while 0 < n + 1 <= 100 and arr[i][n + 1] == 1:
                    n = n + 1
                    cnt += 1
        if cnt < mn : #최소값
            mn = cnt
            short = n
    print(f'#{T} {short-1}')