def dfs(n, sm):
    global ans
    if sm > N: #가지치기
        return

    if n == N:
        if sm == N:
            ans += 1
        return

    for i in range(1, 4):
        dfs(n+1, sm+i)

T = int(input())
for _ in range(T):
    N = int(input())
    ans = 0
    dfs(0, 0)
    print(ans)