def dfs(n, cnt, lst):
    global ans
    if n == N+1:
        if cnt == M:
            ans.append(lst)
            return
        return
    dfs(n+1, cnt+1, lst+[n])
    dfs(n+1, cnt, lst)

N, M = map(int, input().split())
ans = []
dfs(1, 0, [])
for i in range(len(ans)):
    print(*ans[i])