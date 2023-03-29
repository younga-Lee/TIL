def dfs(i, j, sm):
    global ans
    if i == N or j == N:  # 범위를 벗어날 때
        return
    if ans <= sm:  # sm이 ans보다 크다면 더 계산하지 않아도 벗어나자
        return
    if i == N - 1 and j == N - 1: #도착했을 때
        ans = sm
        return

    dfs(i + 1, j, sm + arr[i][j])
    dfs(i, j + 1, sm + arr[i][j])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 10 ** N

    dfs(0, 0, 0)
    ans += arr[N - 1][N - 1]  # 도착 지점 더하기
    print(f'#{tc} {ans}')