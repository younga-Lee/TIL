import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for ts in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for n in range(N)]

    ans = ''

    #가로
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                ans = arr[i][j:j+M]
                break

    #세로
    for i in range(N):
        word = ''
        for j in range(N): #이거 다 가져와야하는데 안가져와서 계속 틀림 ㅠㅠ
            word += arr[j][i]

        for k in range(N-M+1):
            if word[k:k+M] == word[k:k+M][::-1]:
                ans = word[k:k+M]
                break

    print(f'#{ts} {ans}')