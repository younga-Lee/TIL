for _ in range(10):
    ts = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    mx = 0

    # 가로
    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[i][j]
        if total > mx:
            mx = total
    # 세로
    for j in range(100):
        total = 0
        for i in range(100):
            total += arr[i][j]
        if total > mx:
            mx = total

    # 대각선
    for i in range(100):
        total = 0
        total += arr[i][i]
        if total > mx:
            mx = total
    for i in range(100):
        total = 0
        total += arr[99 - i][i]
        if total > mx:
            mx = total
    print(f'#{ts} {mx}')