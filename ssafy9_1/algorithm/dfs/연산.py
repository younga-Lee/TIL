from collections import deque

def bfs(s, e):
    q = deque()
    #초기값
    v = [0] * 1000001
    q.append(s)
    v[s] = 1

    while q:
        c = q.popleft()
        if c == e:
            return v[c] - 1
        for n in ((c + 1), (c - 1), (c * 2), (c - 10)):
            if 1 <= n <= 1000000 and v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    ans = bfs(N, M)
    print(f'#{tc} {ans}')
















# def cal(j, sm):
#     if j == 2:
#         return sm+1
#     if j == 3:
#         return sm-1
#     if j == 1 :
#         return sm*2
#     if j == 0:
#         return sm-10
#
# def dfs(cnt, sm): #연산개수, 합
#     global ans
#     if cnt >= M:
#         return
#
#     if sm < 0 or sm >= M : #종료조건
#         if sm == M:
#             ans = min(cnt, ans)
#             return
#
#     for j in range(4):
#         dfs(cnt+1, cal(j, sm))
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     v = [0]*4
#     ans = M
#     dfs(0, N)
#     print(ans)