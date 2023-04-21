from collections import deque
def bfs1(i, j):
    q = deque([(i, j)])
    v1[i][j] = 1
    color = arr[i][j]
    while q:
        si, sj = q.popleft()
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            ni, nj = si+di, sj+dj
            if 0<=ni<N and 0<=nj<N and v1[ni][nj] == 0 and arr[ni][nj] == color:
                v1[ni][nj] = 1
                q.append((ni, nj))

def bfs2(i, j):
    q = deque([(i, j)])
    v2[i][j] = 1
    color = arr[i][j]
    if color == 'B':
        while q:
            si, sj = q.popleft()
            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                ni, nj = si+di, sj+dj
                if 0<=ni<N and 0<=nj<N and v2[ni][nj] == 0 and arr[ni][nj] == color:
                    v2[ni][nj] = 1
                    q.append((ni, nj))

    else:
        while q:
            si, sj = q.popleft()
            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                ni, nj = si+di, sj+dj
                if 0<=ni<N and 0<=nj<N and v2[ni][nj] == 0 and arr[ni][nj] != "B":
                    v2[ni][nj] = 1
                    q.append((ni, nj))

N = int(input())
arr = [list(input()) for _ in range(N)]
v1 = [[0]*N for _ in range(N)]
v2 = [[0]*N for _ in range(N)]
cnt1 = 0
cnt2 = 0

for i in range(N):
    for j in range(N):
        if v1[i][j] == 0:
            bfs1(i, j)
            cnt1 += 1

for i in range(N):
    for j in range(N):
        if v2[i][j] == 0:
            bfs2(i, j)
            cnt2 += 1

print(cnt1, cnt2)
#bfs일 때 break문 하지 말 것!!
