def turn(i, j):
    dr = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    r = 0
    while r != 4:
        ni, nj = i + dr[r][0], j + dr[r][1]
        if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0:
            v[ni][nj] = arr[i][j]
            i, j = ni, nj
        else:
            r += 1


N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
for _ in range(R):
    for i in range(N//2):
        turn(i, i)
    arr = v
    v = [[0] * M for _ in range(N)]

for k in range(N):
    print(*arr[k])