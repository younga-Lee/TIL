def promising(i, j):
    for di, dj in [[-1, -1], [-1, 0], [-1, 1]]:
        ni, nj = i+di , j+dj
        while 0 <=ni< N and 0 <=nj< N:
            if board[ni][nj]: #다른 퀸이 있으면
                return 0      # 실패
            ni, nj = ni+di, nj+dj

    return 1


def dfs(i, n): #인덱스(가로), 퀸 놓은 개수
    global cnt
    if n == N :
        cnt += 1
        return
    for j in range(N):
        if promising(i, j):
            board[i][j] = 1
            dfs(i+1, n+1)
            board[i][j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0]*N for _ in range(N)]
    cnt = 0

    dfs(0, 0)

    print(f'#{tc} {cnt}')