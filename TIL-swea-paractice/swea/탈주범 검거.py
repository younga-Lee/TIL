import sys
sys.stdin = open("sample_input.txt", "r")

def direction(t):
    dr = []
    if t == 1:
        dr = [(-1, 0), (1, 0), (0, -1), (0, 1)] #상하좌우
    if t == 2:
        dr = [(-1, 0), (1, 0)]
    if t == 3:
        dr = [(0, -1), (0, 1)]
    if t == 4:
        dr = [(-1, 0), (0, 1)]
    if t == 5:
        dr = [(1, 0), (0, 1)]
    if t == 6:
        dr = [(1, 0), (0, -1)]
    if t == 7:
        dr = [(-1, 0),(0, -1)]
    return dr

def dfs(L):
    global ans
    visited = [[0]*M for _ in range(N)]
    stack = [] #위치 저장 stack
    link = {(-1, 0): [1, 2, 5, 6], (1, 0): [1, 2, 4, 7], (0, 1): [1, 3, 6, 7], (0, -1): [1, 3, 4, 5]}
    ans.append((R, C))

    si, sj = R, C #시작점
    visited[si][sj] = 1 #시작점 방문
    sL = L

    while True:
        t = arr[si][sj] #방향번호
        dr = direction(t)  #방향
        for di, dj in dr:
            ni, nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and sL >= 0 and arr[ni][nj] in link[(di, dj)]:
                visited[ni][nj] += 1
                stack.append((si, sj))
                ans.append((ni, nj))
                si, sj = ni, nj #위치변경
                sL -= 1
                break
        else: #더이상 방문할 수 없다면 + sL이 끝났다면
            if stack:
                si, sj = stack.pop()
                sL += 1
            else:
                break

T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int,input().split()) #지하터널 세로길이, 가로길이/ 맨홀뚜껑위치 세로, 가로/ 탈출 후 소요된 시간
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    dfs(L-1)
    print(f'#{tc}',len(ans))



