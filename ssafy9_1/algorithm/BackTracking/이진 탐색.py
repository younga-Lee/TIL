def bs(s, e, d):
    dr = 0
    while s <= e:
        m = (s + e) // 2
        if lst[m] == d:  # 데이터를 찾은 경우
            return 1
        elif lst[m] < d:  # 오른쪽
            if dr == 1:
                return 0
            dr = 1
            s = m + 1
        else:  # 왼쪽
            if dr == -1:
                return 0
            dr = -1
            e = m - 1
    # 찾는 숫자가 없는 경우
    return 0


T = int(input())
for t_c in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))

    lst.sort()
    ans = 0
    for d in lst2:
        ans += bs(0, N - 1, d)
    print(f'#{t_c} {ans}')