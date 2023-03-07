T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    total = 0

    mx_idx = -1
    for i in range(N-2, -1, -1):
        if lst[mx_idx] > lst[i]:
            total += lst[mx_idx]-lst[i]
        else:
            mx_idx = i

    print(f'#{tc} {total}')