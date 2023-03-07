import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    ans = 0

    #시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
                break

    q = [(si, sj)]
    visited[si][sj] = 1

    #BFS
    while q:
        qi, qj = q.pop(0) #이게 젤 중요!!!!!!!!!
        for ri,rj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ni, nj = qi+ri, qj+rj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni, nj))
                visited[ni][nj] += visited[qi][qj] + 1
                if arr[ni][nj] == 3:
                    ans = visited[qi][qj] -1 #끝까지간 것에서 1빼기

    print(f'#{tc} {ans}')