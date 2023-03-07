def cnt(Px, r, l=1):
    sm = 0
    while l <= r:
        c = int((l + r) / 2)
        if c == Px:
            break
        elif c > Px:  # 왼쪽
            r = c
        else:  # 오른쪽
            l = c
        sm += 1
    return sm


T = int(input())

for ts in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())  # 전체쪽수, A가 찾을 페이지, B가 찾을 페이지
    r = P
    ans = 0

    A = cnt(Pa, r)
    B = cnt(Pb, r)

    if A == B:
        ans = 0
    elif A > B:
        ans = 'B'
    else:
        ans = 'A'
    print(f'#{ts} {ans}')