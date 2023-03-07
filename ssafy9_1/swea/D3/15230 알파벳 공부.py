import sys
sys.stdin = open("sample_input.txt", "r")

alpha = 'abcdefghijklmnopqrstuvwxyz'

T = int(input())
for ts in range(1, T+1):
    s = input()
    ans = 0
    for i in range(len(s)):
        if alpha[i] == s[i]:
            ans += 1
        else: break
    print(f'#{ts} {ans}')