def check(cnt):
    for i in range(12):
        if cnt[i] >= 3:  # triplet
            cnt[i] -= 3
            return False

        if cnt[i] >= 1 and cnt[i + 1] >= 1 and cnt[i + 2] >= 1:  # run
            cnt[i] -= 1
            cnt[i + 1] -= 1
            cnt[i + 2] -= 1
            return False
    return True

def dfs(n, tlst):
    global ans
    if n == N:
        if check(tlst):
            ans = 1
        return
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, tlst+[arr[j]])
            v[j] = 0

T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, list(input())))
    N = len(arr)  # 목적지 합
    v = [0] * N
    ans = 0

    dfs(0, )

    print(f'#{tc} {ans}')