import sys
sys.stdin = open("input.txt", "r")


for _ in range(10):
    T = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    # 출구 찾기
    for x in range(100):
        if arr[-1][x] == 2:
            n = x

    # 위로 올라가기
    for i in range(98, -1, -1):
        if arr[i][n - 1] == 1:
            while 0 < n - 1 <= 100 and arr[i][n - 1] == 1 :
                n = n - 1
        elif arr[i][n + 1] == 1:
            while 0 < n + 1 <= 100 and arr[i][n + 1] == 1 :
                n = n + 1
    print(f'#{T} {n-1}')

