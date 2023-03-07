import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split()) #노드개수,간선정보
    arr = [[] for _ in range(V+1)] #개수는 1부터 시작하니까 1 추가
    visited = [0]*(V+1)
    ans = 0

    #간선정보저장
    for _ in range(E):
        s, e = map(int, input().split())
        arr[s].append(e)
        arr[e].append(s)

    S, G = map(int, input().split()) #출발 - 도착
    #왜.. 숫자 순서가 바뀌지..?

    q = [S]
    visited[S] = 1
    while q:
        t = q.pop(0)
        for v in arr[t]:
            if visited[v] == 0:
                q.append(v)
                visited[v] = visited[t]+1
            if v == G:
                ans = visited[v] - 1
                break

    print(f'#{tc} {ans}')