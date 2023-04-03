def bfs(si, sj):
    q = []
    v = [[10**N] * N for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = arr[si][sj]

    while q:
        ci, cj = q.pop(0)

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] > v[ci][cj] + arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + arr[ni][nj]

    return v[N-1][N-1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    ans = bfs(0, 0)
    print(f'#{tc} {ans}')
