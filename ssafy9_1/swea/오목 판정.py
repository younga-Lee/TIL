# import sys
# sys.stdin = open("s_input.txt", "r")

#다섯 개 이상 연속한 부분이 있는지 없는지
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = 'NO'

    #가로
    for i in range(N): #row
        for j in range(N-4):
            if arr[i][j] == arr[i][j+1] == arr[i][j+2] == arr[i][j+3] == arr[i][j+4] == 'o':
                ans = 'YES'
                break
    #세로
    arr2 = list(zip(*arr))
    for i in range(N):
        for j in range(N - 4):
            for k in range(5):
                if arr[i][j] == arr[i][j+k]
                    ans = 'YES'
                break

    #대각선
    for i in range(N-4):
        for j in range(N-4):
            if arr[i][j] == arr[i+1][j+1] == arr[i+2][j+2] == arr[i+3][j+3] == arr[i+4][j+4] == 'o':
                ans = 'YES'
                break

    for i in range(N-4):
        for j in range(N-1, 3, -1):
            if arr2[i][j] == arr2[i+1][j-1] == arr2[i+2][j-2] == arr2[i+3][j-3] == arr2[i+4][j-4] == 'o':
                ans = 'YES'
                break


    print(f'#{tc} {ans}')
