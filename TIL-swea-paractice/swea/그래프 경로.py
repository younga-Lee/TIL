import sys
sys.stdin = open("s_input.txt", "r")


def dfs(s):
    stk = []

    while True:
        for e in adj[s]:  # s에 연결된 노드를 순차적으로 처리
            if v[e] == 0:  # 미 방문
                stk.append(s)

                s = e
                v[s] = 1
                break
        else:  # 더이상 탐색할 노드 없는 경우=>직전으로 돌아감
            if stk:
                s = stk.pop()
            else:
                break


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)

    S, G = map(int, input().split())
    v = [0] * (V + 1)
    dfs(S)  # 찾아도 끝까지 실행
    print(f'#{test_case} {v[G]}')


