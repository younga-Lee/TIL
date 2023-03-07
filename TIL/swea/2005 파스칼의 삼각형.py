T = int(input())

for ts in range(1, T+1):
    N = int(input())
    arr = [[1]*i for i in range(1, N+1)]

    for i in range(2, N):
        for j in range(1, i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{ts}')
    for _ in range(len(arr)):
        print(*arr[_])

#잘 모르겠을 땐 프린트 해보기!
#문제풀때는 범위 설정 확인이 가장 중요한 것 같다