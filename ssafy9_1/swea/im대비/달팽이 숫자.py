T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    dr = [(0, 1), (1, 0), (0, -1), (-1, 0)] #오른쪽, 아래, 왼쪽, 위

    #초기값 설정
    i, j, r = 0, 0, 0
    for n in range(1, N*N+1): #숫자 입력
        arr[i][j] = n
        visited[i][j] = 1

        ni, nj = i + dr[r][0], j + dr[r][1]
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            i, j = ni, nj
        else:
            r = (r+1)%4
            i, j = i + dr[r][0], j + dr[r][1]

    print(f'#{tc}')
    for n in range(N):
        print(*arr[n])
