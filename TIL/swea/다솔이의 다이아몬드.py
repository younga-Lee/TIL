import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for ts in range(1, T+1):
    word = list(input())
    N = 5 + 4*(len(word)-1)
    arr = [['.']*N for _ in range(N)]


    for i in range(5):
        w = 0
        for j in range(N):
            if i%2: #홀수면
                if j%2:
                    arr[i][j] = '#'
            else:
                if (j+2)%4 == 0:
                    arr[i][j], arr[2][j-2], arr[2][j + 2] = '#'*3
                    arr[2][j] = word[w]
                    w += 1

    for _ in range(5):
        print(''.join(arr[_]))