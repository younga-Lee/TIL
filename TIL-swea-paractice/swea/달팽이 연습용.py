T = 1
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for ts in range(1, T+1):
    N = 3
    arr = [[0 for _ in range(N)] for _ in range(N)]

    i = j = dr = 0
    for cnt in range(1, N*N+1):
        arr[i][j] = cnt
        ni, nj = i + di[dr], j + dj[dr]

        if 0 <= ni <N and 0 <= nj <N and arr[ni][nj] == 0:
            i, j = ni, nj
        else:
            dr = (dr+1)%4
            i, j = i + di[dr], j + dj[dr]

    print(f'#{ts}, {arr}')
    for i in range(N):
        print(*arr[i])