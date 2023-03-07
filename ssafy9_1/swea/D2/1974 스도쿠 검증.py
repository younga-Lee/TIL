import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for ts in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1

    #세칸씩
    for n in range(0, len(arr), 3):
        for i in range(3):
            num = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            for j in range(3):
                one_line = arr[n + j][i * 3:(i + 1) * 3]
                for k in one_line:
                    if num[k] == 0:
                        num[k] = 1
                    else:
                        ans = 0
                        break
    #가로
    for i in range(9):
        if len(set(arr[i])) != 9:
            ans = 0
            break
    #세로
    arr2 = list(zip(*arr))
    for i in range(9):
        num = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for j in range(9):
            if num[arr2[i][j]] == 0:
                num[arr2[i][j]] = 1
            else:
                ans = 0

    print(f'#{ts} {ans}')