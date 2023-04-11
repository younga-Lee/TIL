from collections import deque
def bfs(i, j):
    visited = [[0] * M for _ in range(N)]
    cnt = 1
    q = deque()
    q.append((i, j))
    while q:
        t = q.popleft()
        visited[t] = 1
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i+di, j+dj
            if ni == N and nj == M:
                return
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0:
                q.append((ni, nj))
                cnt += 1


N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]

bfs(0, 0)

print(arr)