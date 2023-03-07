import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    ans = 0

    si, sj, ei, ej = 0, 0, 0, 0
    #출발, 도착 위치 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
            elif arr[i][j] == 3:
                ei, ej = i, j

    q = [(si, sj)]
    visited[si][sj] = 1
    dr = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # 오른/왼/아래/위
    #미로찾기
    while q:
        qi, qj = q.pop(0)
        for r in range(4): #네 방향을 모두 보기
            ni, nj = qi+dr[r][0], qj+dr[r][1]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni, nj))
                visited[ni][nj] = 1
                if arr[ni][nj] == 3:
                    ans = 1
                    break

    print(f'#{tc} {ans}')
