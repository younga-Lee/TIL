def dfs(n, sm, cnt): #인덱스, 잔량, 개수
    global mn
    if mn <=cnt:
        return
    if n == N: #종료조건
        if mn > cnt:
            mn = cnt
        return

    dfs(n + 1, arr[n]-1, cnt + 1)
    if sm > 0: #잔량이 남아있을 경우
        dfs(n + 1, sm-1, cnt)

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]-1
    arr = arr[1:]

    mn = 100000
    dfs(1, arr[0]-1, 0)

    print(f'#{tc} {mn}')