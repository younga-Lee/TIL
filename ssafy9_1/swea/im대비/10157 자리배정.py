C, R = map(int, input().split()) #공연장의 크기
K = int(input()) #관객 대기 번호
arr = [[0] * C for _ in range(R)]
visited = [[0] * C for _ in range(R)]

dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]

if K > C*R:
    print(0)
else:
    i, j, r = R-1, 0, 0
    for n in range(1, K+1):
        arr[i][j] = n
        visited[i][j] = 1
        if n == K: #원하는 번호가 나오면 브레이크
            break
        ni, nj = i + dr[r][0], j +dr[r][1]
        if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0:
            i, j = ni, nj
        else:
            r = (r+1)%4
            ni, nj = i + dr[r][0], j + dr[r][1]
            i, j = ni, nj

    x, y = j + 1, R-i

    print(x, y)

