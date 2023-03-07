import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    p = list(map(int, input().split()))
    r = 0
    mx = p[-1]

    for i in range(len(p)-2, -1, -1):
        if mx > p[i]:
            r += mx-p[i]
        else:
            mx = p[i]


    print(f'#{tc} {r}')