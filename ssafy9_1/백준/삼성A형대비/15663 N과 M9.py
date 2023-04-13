def dfs(cnt,  lst):
    if cnt == M:
        ans.add(tuple(lst))
        return
    for i in range( N):
        dfs(cnt+1, lst + [num[i]])

N, M = map(int, input().split())
num = sorted(map(int, list(input().split())))
ans = set()
v = [0]*N
dfs(0, [])

for lst in sorted(ans):
    print(*lst)