T = int(input())

for tc in range(1, T+1):
    n = float(input())
    ans = ''
    while n != 1.0:
        n *= 2
        if n == 1:
            ans += '1'
        elif n > 1:
            n -= 1
            ans += '1'
        else:
            ans += '0'

        if len(ans) > 13:
            ans = 'overflow'
            break


    print(f'#{tc} {ans}')