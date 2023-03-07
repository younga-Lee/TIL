import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    tc = int(input())
    arr = [[0]+ list(map(int, input().split())) +[0] for _ in range(100)]

    n = arr[-1].index(2) #출구 인덱스

    #거꾸로 올라오자
    i = 99
    for i in range(98, -1, -1):
        if arr[i][n - 1] == 1:
            while 0 < n - 1 <= 100 and arr[i][n - 1] == 1:
                n = n - 1
        elif arr[i][n + 1] == 1:
            while 0 < n + 1 <= 100 and arr[i][n + 1] == 1:
                n = n + 1
    print(f'#{tc} {n-1}')