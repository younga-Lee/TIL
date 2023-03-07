import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr2 = list(zip(*arr))
    result, result2 = 0, 0

    for k in range(M, 1, -1):
        for i in range(N):  # row
            ans = 0
            for j in range(M):  # column:
                if arr[i][j] == 1:
                    ans += 1
                    if ans == k:
                        result = ans
                        break
                else:
                    ans = 0
            if ans == k:
                result = ans
                break
        if ans == k:
            result = ans
            break

    for k in range(N, 1, -1):
        for i in range(M):  # row
            ans = 0
            for j in range(N):  # column:
                if arr2[i][j] == 1:
                    ans += 1
                    if ans == k:
                        result2 = ans
                        break
                else:
                    ans = 0
            if ans == k:
                result2 = ans
                break
        if ans == k:
            result2 = ans
            break

    if result2 > result:
        result = result2

    print(f'#{tc} {result}')


