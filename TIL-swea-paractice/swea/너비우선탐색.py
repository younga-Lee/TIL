T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)] #인접리스트

    for i in range(E):
        v1, v2 = map(int, input().split())
        adjL[v1].append(v2)
        adjL[v2].append(v1)

    visited = [0] * (V+1)
    q = [1] #시작점을 넣은 큐

    visited[1] = 1
    path = []
    while q:
        t = q.pop(0)
        path.append(t)
        for v in adjL[t]:
            if visited[v] == 0:
                q.append(v)
                visited[v] = visited[t] + 1 #몇번째 depth인지

    print(f'#{tc}', *path)
