from collections import deque

def bfs(i, j):
    #초기값
    q = deque([(i, j)])
    while q:
        si, sj = q.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni = si+di
            nj = sj+dj

            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1: #이동가능한칸 + 범위내
                q.append((ni, nj))
                arr[ni][nj] += arr[si][sj]

    return arr[N-1][M-1]

N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]
print(bfs(0, 0))