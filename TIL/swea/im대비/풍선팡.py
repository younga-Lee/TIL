T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    dr = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(0, N):
        for j in range(0, M):
            val = arr[i][j]
            total = val
            for di, dj in dr:
                for v in range(1, val + 1):
                    ni, nj = i+di*v, j+dj*v
                    if 0<=ni<N and 0<= nj < M:
                        total += arr[ni][nj]
            if total > mx:
                mx = total

    print(f'#{tc} {mx}')
