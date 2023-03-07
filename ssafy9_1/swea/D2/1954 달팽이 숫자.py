import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 방향 바꿀 때
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for ts in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)] #빈칸

    i = j = dr = 0
    for n in range(1, N*N+1):
        arr[i][j] = n
        ni, nj = i + dx[dr], j + dy[dr]

        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0: #인덱스가 범위안에 있다면
            i, j = ni, nj
        else:
            dr = (dr+1)%4
            i, j =  i + dx[dr], j + dy[dr]

    print(arr)
