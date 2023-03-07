import sys
sys.stdin = open("s_in1.txt", "r")

def check(dr):
    mx = 0
    for i in range(1, N):
        for j in range(1, N):
            total = 0
            for di, dj in dr:
                for k in range(1, M): #순서 바꾸기
                    ni, nj = i+di*k, j+dj*k #변수명 잘못써서 한참걸림
                    if 0 <= ni < N and 0 <= nj < N:
                        total += arr[ni][nj]
            total += arr[i][j]
            if total > mx:
                mx = total
    return mx

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]

    dr1 = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
    dr2 = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    print(f'#{tc}', check(dr1) if check(dr1) > check(dr2) else check(dr2))
