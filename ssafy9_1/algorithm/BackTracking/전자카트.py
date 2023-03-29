def perm(n, sm):
    global ans
    if n == N: #종료시점
        ans = min(ans, sm)
        return
    for j in range(N):
        v[n] = 1
        if v[j] == 0:
            v[j] = 1
            perm(n + 1, sm + arr[n][j])
            v[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N
    ans = 10**N

    perm(0, 0)

    print(ans)