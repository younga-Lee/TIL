def dfs(i, j):
    stk = []
    stk.appen
    for di, dj in [(0,1),(0,-1),(-1,0),(1,0)]:
        ni,nj = di+i, dj+j
        if v[ni][nj]==0:
            cnt += 1
            break

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
v = [[0]*N for _ in range(N)]
cnt = 0
#위아래양옆이 모두 1이면 안됨
