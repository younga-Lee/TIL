T = int(input())

for ts in range(1, T+1):
    N = int(input())

    ans =0
    for n in range(1,N+1):
        if n%2 == 0: ans -= n
        else: ans += n

    print(f'#{ts} {ans}')
#넘 쉬움
