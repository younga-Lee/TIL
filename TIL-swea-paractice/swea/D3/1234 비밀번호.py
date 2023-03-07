import sys
sys.stdin = open("input.txt", "r")

for ts in range(1, 11):
    N, string = input().split()
    N = int(N)

    num = [str(i)*2 for i in range(10)] #연속하는 숫자

    for i in range(N):
        for n in num:
            if n in string: string = string.replace(n, '') #붙어있는 숫자 지우기

    print(f'#{ts} {string}')