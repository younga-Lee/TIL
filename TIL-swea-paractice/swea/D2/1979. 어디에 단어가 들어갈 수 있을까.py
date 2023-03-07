import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for ts in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    #가로
    for i in range(N):
        one = 0
        for j in range(N):
            if arr[i][j] == 1:
                one += 1
                if j == (N-1) and one == K: #단어퍼즐의 개수가 K일 때
                    ans += 1
            else: #0일 때
                if one == K: #0이기 전까지의 단어퍼즐 개수가 K일 때
                    ans += 1
                one = 0

    #세로
    for j in range(N):
        one = 0
        for i in range(N):
            if arr[i][j] == 1:
                one += 1
                if i == (N - 1) and one == K:
                    ans += 1
            else:
                if one == K:
                    ans += 1
                one = 0

    print(f'#{ts} {ans}')
