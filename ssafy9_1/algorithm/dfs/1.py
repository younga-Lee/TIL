def cal(j, sm):
    if j == 2:
        return sm+1
    if j == 3:
        return sm-1
    if j == 1 :
        return sm*2
    if j == 0:
        return sm-10

def dfs(cnt, sm): #연산개수, 합
    q = []


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    v = [0]*4
    ans = M
    dfs(0, N)
    print(ans)