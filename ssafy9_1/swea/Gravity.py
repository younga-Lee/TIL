T = int(input())

for ts in range(1, T+1):
    ans = 0
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(0, N):
        cnt = 0
        for j in range(i+1, N) : #i부터 끝까지
            if arr[i] > arr[j]: #나보다 작으면
                cnt += 1
            if ans < cnt:
                ans = cnt
    print(f'#{ts} {ans}')