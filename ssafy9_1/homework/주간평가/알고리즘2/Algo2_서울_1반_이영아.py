T = int(input())

for tc in range(1, T+1):
    N = int(input()) #NxN
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}   #0, 1, 2, 3 이동방향
    visited = [[0]*N for _ in range(N)] #지나간 구역은 다시 지나가지 않는다
    energy = []

    #에너지 방향
    i, j = 0, 0 #시작점
    while True:
        energy.append(arr[i][j])
        r = arr[i][j]
        ni, nj = i + dr[r][0], j + dr[r][1] #새로운 위치
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] != 1: #범위 안에 있고 방문하지 않았다면
            visited[ni][nj] = 1
            i, j = ni, nj
        else:
            break

    #에너지 소비 나타내기
    cost = []
    for e in range(len(energy)):
        if energy[e-1] != energy[e]:
            cost.append(energy[e])

    print(f'#{tc}', *cost)