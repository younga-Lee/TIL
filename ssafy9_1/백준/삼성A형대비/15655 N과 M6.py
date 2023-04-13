def dfs(cnt, lst, index):
    if cnt == M:
        ans.append(lst)
        return
    for i in range(index, N):
        dfs(cnt+1, lst + [num[i]], i+1)

N, M = map(int, input().split())
num = sorted(map(int, list(input().split())))
ans = []
dfs(0, [], 0)
for k in range(len(ans)):
    print(*ans[k])