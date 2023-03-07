import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [(1, 0), (-1, 0), (0, -1), (0, 1)] #상, 하, 좌, 우

    def check(i, j):
        r = 0 ; cnt = 1
        si, sj = i, j
        while r < 4:
            ni, nj = si + dr[r][0], sj + dr[r][1]
            if 0 <= ni < N and 0 <= nj < N and arr[si][sj] + 1 == arr[ni][nj]: #범위 내 + 1증가
                si, sj = ni, nj
                cnt += 1
            else:
                r += 1
        return cnt

    ans = []
    a = []
    for i in range(N):
        for j in range(N):
            v = check(i, j)
            ans.append(v)
            a.append(arr[i][j])
    print(max(ans))
