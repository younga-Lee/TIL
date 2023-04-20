from collections import deque
def bfs(i, j):
    q = deque([(i, j)])
    cnt = 0
    while q:
        i, j = q.popleft()
        for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1:
                q.append((ni, nj))
                arr[ni][nj] = 0
                cnt += 1
                #break를 하면 탐색할 때 다시 돌아갈 수 없음..
    if cnt == 0:
        cnt = 1
    return cnt

N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
num = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            num.append(bfs(i, j))
print(len(num))
for n in sorted(num):
    print(n)