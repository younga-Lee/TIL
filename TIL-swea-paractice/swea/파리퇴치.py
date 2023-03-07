import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for si in range(N-M+1):
        for sj in range(N-M+1):
            cnt = 0
            for i in range(si, si+M):
                for j in range(sj, sj+M):
                    cnt += arr[i][j]
            if cnt > ans:
                ans = cnt
    print(f'#{tc} {ans}')