import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for ts in range(1, T+1):
    N = int(input()) #N x N 행렬
    arr = [ input().split() for _ in range(N)]
    a1 = [[0]*N for _ in range(N)]
    a2 = [[0] * N for _ in range(N)]
    a3 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            a1[i][j] = arr[N-1-j][i]
            a2[i][j] = arr[N - 1 - i][N-1-j]
            a3[i][j] = arr[j][N-1-i]

    print(f'#{ts}')
    for a, b, c in zip(a1, a2, a3):
        print(f'{"".join(a)} {"".join(b)} {"".join(c)}')

