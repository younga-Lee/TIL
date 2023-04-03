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

# def dfs(s):
#     # 방문표시: 첫 방문시 처리할 일 있으면 이곳에서..!
#     v[s] = 1
#     alst.append(s)
#
#     for e in adj[s]:
#         if v[e] == 0:  # 연결된 노드이고 미방문시
#             dfs(e)


def bfs(s):
    # [1] q, v[] 생성, 필요시 flag 생성
    q = []

    # [2] q에 초기데이터 삽입(단위 작업)
    v[s] = 1
    q.append(s)
    alst.append(s)

    while q:
        c = q.pop(0)

        # [3] 4/8방향, 연결된노드 등 미방문, 조건맞으면 Q삽입
        for e in adj[c]:
            if v[e] == 0:
                v[e] = 1
                q.append(e)
                alst.append(e)

    # 가능한 모든 위치 탐색 완료후 필요시 특정값 리턴


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)  # 양방향 연결이므로..

    # 여러개 연결시 낮은번호부터 방문! => 오름차순 정렬!!!
    for i in range(1, V + 1):
        adj[i].sort()

    alst = []
    v = [0] * (V + 1)

    # dfs(1)
    bfs(1)

    print(f'#{test_case}', *alst)
