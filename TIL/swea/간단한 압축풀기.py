import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for ts in range(1, T+1):
    N = int(input())
    ans = []
    for n in range(N):
        a, n = input().split()
        n = int(n)
        ans.append(a*n)
    lst = ''.join(ans)

    print(f'#{ts}')
    #10너비로 출력
    a = 0
    for l in lst:
        a += 1
        print(l, end='')
        if a % 10 == 0:
            print()
    print()