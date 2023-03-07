T = int(input())

for ts in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for n in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            for di, dj in  ((-1,0),(1,0),(0,-1),(0,1)): #4방향
                ni, nj = i +di, j+dj #새로운 위치
                print(ni, nj)
                if 0 <= ni < N and 0 <= nj < N: #범위내인지 확인
                    if arr[i][j] > arr[ni][nj]:
                        ans += (arr[i][j] - arr[ni][nj])
                    else:
                        ans += (arr[ni][nj] - arr[i][j])

    print(f'#{ts} {ans}')
