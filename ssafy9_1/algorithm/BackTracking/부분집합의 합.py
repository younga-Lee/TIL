def dfs(n, cnt, sm):
    global ans
    if n == N:
        if cnt == CNT and sm == K:
            ans += 1
        return

    dfs(n + 1, cnt + 1, sm + lst[n]) #선택하였을 때
    dfs(n + 1, cnt, sm) #안하였을때



T = int(input())
for tc in range(1, T + 1):
    CNT, K = map(int, input().split()) #부분집합 원소의 수, 부분집합의 합
    N = 12
    lst = [n for n in range(1, N + 1)]
    ans = 0
    dfs(0, 0, 0)
    print(f'#{tc} {ans}')



