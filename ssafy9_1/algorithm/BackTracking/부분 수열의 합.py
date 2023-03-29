def dfs(n, sm):
    global cnt
    if n == N: #종료 조건
        return
    if sm >= K:
        if sm == K :
            cnt += 1
        return

    for i in range(n+1, N):
        if v[i] == 0:
            v[i] = 1
            dfs(n + 1, sm+arr[n])
            v[i] = 0

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    v = [0]*N #방문
    cnt = 0
    dfs(0, 0)

    print(f'#{tc} {cnt}')