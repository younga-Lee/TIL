T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    s, e = 1, N
    ans = -1
    while s <= e:
        m = (s + e) // 2
        if N == m ** 3:
            ans = m
            break
        elif N < m ** 3:
            e = m - 1
        else:
            s = m + 1

    print(f'#{tc} {ans}')

    #이분탐색으로 안하면 시간 초과 뜸