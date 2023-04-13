def dfs(cnt, lst):
    if cnt == M:
        ans.append(lst)
        return
    for i in range(1, N+1):
        if i not in lst:
            dfs(cnt+1, lst+[i])

N, M = map(int, input().split())
ans = []
dfs(0, [])

for k in range(len(ans)):
    print(*ans[k])
