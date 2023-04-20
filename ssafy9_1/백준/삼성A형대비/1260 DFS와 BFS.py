from collections import deque
def bfs(start):
    q = deque([start])
    visited[start] = 1
    while q:
        top = q.popleft()
        for i in lst[top]:
            if visited[i] == 0:
                q.append(i)
                b.append(i)
                visited[i] = 1

def dfs(start):
    visited[start] = 1
    d.append(start)
    for i in lst[start]:
        if visited[i] == 0:
            dfs(i)

N, M, V = map(int, input().split())
lst=[[] for _ in range(N+1)]
d = []
b = [V]
for _ in range(M):
    A, B = map(int, input().split())
    lst[A].append(B)
    lst[B].append(A)
    lst[A].sort()
    lst[B].sort()

visited = [0]*(N+1)

dfs(V)
print(*d)

visited = [0]*(N+1)

bfs(V)
print(*b)
