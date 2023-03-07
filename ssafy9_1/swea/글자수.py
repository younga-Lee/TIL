import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for ts in range(1, T+1):
    str1 = input()
    str2 = input()

    d = {}
    for i in str1:
        d[i] = 0

    for s in str2:
        if s in str1:
            d[s] += 1

    mx = 0
    for v in d.values():
        if mx < v:
            mx = v

    print(f'#{ts} {mx}')