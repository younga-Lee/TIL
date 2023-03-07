import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N, s = map(int, input().split()) #입력받는 길이, 시작점
    num = list(map(int, input().split()))
    V = max(num) #노드 개수

    # 간선정보
    arr = [[] for _ in range(V+1)]
    for i in range(N):
        if i%2:
            arr[num[i-1]].append(num[i])

    visited = [0] * (V + 1)
    q = [s]
    visited[s] = 1
    path = []
    while q:
        t = q.pop(0)
        path.append(t)
        for v in arr[t]:
            if visited[v] == 0: #거쳐지지 않았다면
                q.append(v)
                visited[v] = visited[t] + 1

    #마지막에 연락이 됨
    final = 0
    for p in path:
        if visited[p] == max(visited) and final < p:
            final = p
    print(f'#{tc}', final)