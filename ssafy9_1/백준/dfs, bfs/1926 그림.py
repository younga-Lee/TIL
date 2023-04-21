from collections import deque

def bfs(i, j):
    q = deque([(i, j)])
    arr[i][j] = 2 #이미 사용한 숫자는 2로 바꾸기
    wd = 1 #그림의 넓이 default 1!
    while q:
        si,sj = q.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = si+di, sj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1: #범위안에 있고, 그림(1)일 떄
                arr[ni][nj] = 2
                q.append((ni, nj))
                wd += 1
    return wd

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
mx = 0
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            result = bfs(i, j)
            cnt += 1 #그림개수
            if mx < result:
                mx = result
print(cnt)
print(mx)