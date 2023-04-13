def dfs(n, sm):
    global cnt
    if n == N:
        if sm == K:
            cnt += 1
        return

    dfs(n+1, sm+arr[n])
    dfs(n+1, sm)

N, K = map(int, input().split())
arr = list(map(int, input().split()))

v = [0]*N #방문
cnt = 0
dfs(0, 0)
print(cnt)