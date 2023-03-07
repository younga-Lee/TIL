import sys
input = sys.stdin.readline

n = int(input()) #총라운드수
for _ in range(n*2):
    ans = 'A'
    a = list(map(int, input().split())) #맨앞:총 개수, 나머지: 정수
    if len(a) >= 2:
        cnt_a, lst_a = a[0], a[1:]
    else:
        ans = 'B'
        break

    b = list(map(int, input().split()))
    if len(b) >= 2:
        cnt_b, lst_b = b[0], b[1:]
    else:
        break

    if lst_a.count(4) != lst_b.count(4):
        if lst_a.count(4) < lst_b.count(4):
            ans = 'B'

    elif lst_a.count(3) != lst_b.count(3):
        if lst_a.count(3) < lst_b.count(3):
            ans = 'B'

    elif lst_a.count(2) != lst_b.count(2):
        if lst_a.count(2) < lst_b.count(2):
            ans = 'B'

    elif lst_a.count(1) != lst_b.count(1):
        if lst_a.count(1) < lst_b.count(1):
            ans = 'B'

    else:
        ans = 'D'
    print(ans)
