import sys
sys.stdin = open("input2.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(M+2)] + [[0] + list(map(int, input().split())) +[0] for _ in range(N)]+ [[0]*(M+2)] #액자처럼 패딩
    result = 0

    for i in range(1, N+1):
        for j in range(1, M+1):
            ans = 0
            a = arr[i][j]
            for k in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1,-1)): #8방향
                if 0 < arr[i + k[0]][j + k[1]] < arr[i][j]: #패딩값은 제외(0)
                    ans += 1
            if ans >= 4:
                result += 1

    print(f'#{tc}', result)