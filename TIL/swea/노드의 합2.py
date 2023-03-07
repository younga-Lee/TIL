import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    lst = [0]*(N+1)
    for _ in range(M):
        c, val = map(int, input().split())
        lst[c] = val
        p = c//2
        while c//2 > 0:
            lst[p] += val
            c = p
            p = c//2
    print(f'#{tc} {lst[L]}')