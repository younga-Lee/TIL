import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) #한변의 길이 N, 돌을 놓는 횟수 M
    arr = [[0]*(N+2) for _ in range(N+2)] #액자형식으로 패딩
    dr = [(1, 0), (-1, 0), (0, 1), (0, -1)] #오른, 왼, 위, 아래

    #처음 배치 #흑1, 백2
    arr[N // 2 + 1][N // 2] = arr[N // 2][N // 2 + 1] = 1
    arr[N // 2][N // 2] = arr[N // 2 + 1][N // 2 + 1] = 2

    for _ in range(M):
        x, y, color = map(int, input().split())
        if color == 1: #흑돌
            arr[x][y] = 1

        else:
            arr[x][y] = 2


    print(arr)
    print(f'#{tc}')