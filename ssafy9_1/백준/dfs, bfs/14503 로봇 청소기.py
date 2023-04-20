from collections import deque

def bfs(i, j):
    q = deque([(i, j)])
    dr = [(0, -1)]
    pass

N, M = map(int, input().split())
r, c, d = map(int, input().split()) #처음 좌표, 처음에 바라보는 방향
arr = [list(map(int, input().split())) for _ in range(N)]
bfs(r, c)