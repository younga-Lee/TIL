def dfs(x, y, n, cnt): #위치 x, y, 0의 개수, 비숍의 개수
    global ans
    if n == N**2:
        ans = max(ans, cnt)
        return

    if arr[x][y] == 1:
        tmp = 0
        for dx, dy in dr:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 1:
                arr[nx][ny] = 1
                tmp += 1
        dfs(x, y, n+tmp, cnt+1)



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
first = 0 #처음 0의 개수
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            first += 1
#갈수 있는 방향
dr = []
for di, dj in [(-1, -1), (1, 1), (-1, 1), (1, -1)]:
    for k in range(N):
        dr.append((di*k, dj*k))
print(dr)