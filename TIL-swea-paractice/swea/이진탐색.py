T = int(input())

for ts in range(1, T+1):
    N , D = map(int, input().split())
    arr = list(map(int, input().split()))

    start = 0
    ans = 0
    end = N-1
    while start <= end :
        middle = (start+end)//2
        if arr[middle] == D:
            ans = middle + 1
            break
        elif arr[middle] > D:
            end = middle - 1
        else:
            start = middle + 1

    print(f'#{ts} {ans}')