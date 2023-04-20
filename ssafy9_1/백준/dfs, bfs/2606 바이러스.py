from collections import deque

def bfs(start):
    global cnt
    q = deque([1])
    v[1] = 1
    while q:
        top = q.popleft()
        for i in lst[top]:
            if v[i] == 0:
                v[i] = 1
                q.append(i)
                cnt += 1


N = int(input()) #컴퓨터 수
M = int(input()) #간선 수
lst=[[] for _ in range(N+1)]
v = [0]*(N+1)
cnt = 0
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
    lst[a].sort()
    lst[b].sort()
bfs(1)
print(cnt)