import sys
sys.stdin = open("input.txt", "r")

def check(i, j):
    cnt = 1
    while True:
        r = 0
        dr = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while r < 4 :  # 주변을 보았을 때
            ni, nj = i + dr[r][0], j + dr[r][1]
            if 0 <= ni < N and 0 <= nj < N and arr[i][j] + 1 == arr[ni][nj]:  # 범위에 있고 값이 1증가한다면
                i, j = ni, nj  # 이동
                cnt += 1
                r = 0
            else:
                r += 1
        else:
            return cnt
T = int(input())

for tc in range(1, T+1):
    N = int(input()) #NxN
    arr = [list(map(int, input().split())) for _ in range(N)]

    mx = 0
    mx_num = {}
    for i in range(N):
        for j in range(N):
            check(i, j)
            if mx <= check(i, j):
                mx = check(i, j)
                mx_num[arr[i][j]] = mx
    ans = []
    for k, v in mx_num.items():
        if v == mx:
            ans.append(k)

    print(f'#{tc}', min(ans), mx)

