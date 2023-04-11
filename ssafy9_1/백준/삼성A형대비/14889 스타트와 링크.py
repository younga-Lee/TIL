def dfs(n, sm):
    global ans
    if n == N//2:
        t1.append(sm)
        return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n+1, sm + arr[n][j])
            visited[j] = 0 #초기화

N = int(input()) #NxN
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*N
ans = 0