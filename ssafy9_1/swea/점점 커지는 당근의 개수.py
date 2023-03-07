#연속으로 커지는 당근의 개수

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for ts in range(1, T+1):
    N = int(input()) #당근 개수
    C = list(map(int, input().split()))

    mx = ans = 1
    for c in range(1, N):
        if C[c-1] < C[c] : ans += 1
        else : ans = 1
        if mx < ans : mx = ans

    print(f'#{ts} {mx}')
#--- mx로 해야하는데 자꾸 ans로 출력함 힝 구