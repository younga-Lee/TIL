def dfs(n, sm):
    global ans
    if ans <= sm:  #종료조건
        return
    if n == N:
        ans = sm
        return
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, sm + arr[n][j])
            v[j] = 0 #호출 후 clear

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**N #최소값구하기
    v = [0]*N
    lst = []
    dfs(0, 0)

    print(f'#{tc} {ans}')