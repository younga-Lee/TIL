def dfs(cnt, lst, idx):
    if cnt == M:
        ans.append(lst)
        return
    for i in range(idx, N):
        dfs(cnt+1, lst + [num[i]], i)

N, M = map(int, input().split())
num = sorted(map(int, list(input().split())))
ans = []
dfs(0, [], 0)
for k in range(len(ans)):
    print(*ans[k])