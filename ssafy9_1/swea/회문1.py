import sys
sys.stdin = open("input.txt", "r")

for ts in range(1, 11):
    N = int(input()) #찾아야하는 회문 길이
    arr = [input() for _ in range(8)]
    cnt = 0

    arr2 = list(zip(*arr)) #전치행렬
    for _ in range(8):
        for i in range(8-N+1):
            if arr[_][i:i+N] == arr[_][i:i+N][::-1]:
                cnt += 1
            if arr2[_][i:i + N] == arr2[_][i:i + N][::-1]:
                cnt += 1

    print(f'#{ts}', cnt)
