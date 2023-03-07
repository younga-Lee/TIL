def check(a, b):
    for n in range(a, b+1):
        count[n] += 1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    count = [0]*401 #방의 개수

    for i in range(N):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        if a%2:
            if b%2: check(a, b+1)
            else: check(a, b)
        else:
            if b%2: check(a-1, b+1)
            else: check(a-1, b)

    print(f'#{tc} {max(count)}')
