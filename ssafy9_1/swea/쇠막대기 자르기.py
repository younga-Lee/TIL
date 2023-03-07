import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    iron = list(input())
    stack = []
    ans = 0
    for i in iron:
        if i == '(':
            ans += 1

    print(f'#{tc}', ans)