import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for ts in range(1, T+1):
    N = int(input())

    red = []
    blue = []
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        if color == 1: #빨간색 리스트
            for i in range(r1,r2+1):
                for j in range(c1, c2+1):
                    red.append((i, j))

        if color == 2:#파란색 리스트
            for i in range(r1,r2+1):
                for j in range(c1, c2+1):
                    blue.append((i, j))

        #보라색 찾기
        purple = 0
        for i in red:
            if i in blue:
                purple += 1

    print(f'#{ts} {purple}')