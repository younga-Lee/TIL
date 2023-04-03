'''
1
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''

def dfs(v, k):
    visited[v] = 1
    path.append(v)
    for w in range(1, k+1):
        if adjM[v][w] == 1 and visited[w] == 0:
            dfs(w, k)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjM = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V + 1)  # 중복 방지
    path = []
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjM[n1][n2] = 1
        adjM[n2][n1] = 1
    dfs(1, V)

    print(f'#{tc}',*path)