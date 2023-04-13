def dfs(cnt, lst):
    if cnt == M:
        ans.append(lst)
        return
    for i in range(N):
        if num[i] not in lst:
            dfs(cnt+1, lst + [num[i]])

N, M = map(int, input().split())
num = sorted(map(int, list(input().split())))
ans = []
dfs(0, [])
for k in range(len(ans)):
    print(*ans[k])