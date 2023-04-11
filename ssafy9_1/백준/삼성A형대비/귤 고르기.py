k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]

def dfs(n, cnt, sm):
    global ans
    if cnt == k or N == n:
        if cnt == k:
            ans = min(ans, len(set(sm)))
        return

    dfs(n+1, cnt, sm) #안담을 때
    dfs(n+1, cnt+1, sm+[tangerine[n]]) #담을 때

N = len(tangerine)
ans = 100000

dfs(0, 0, [])
print(ans)