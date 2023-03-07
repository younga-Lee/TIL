#가장 큰 회문 길이
import sys
sys.stdin = open("input.txt", "r")

def check(arr):
    for k in range(99, -1, -1):  # 큰 문자열 길이부터
        for i in range(100):  # 한줄씩
            for j in range(100 - k + 1):
                if arr[i][j:j + k] == arr[i][j:j + k][::-1]:
                    return k
                    exit() #시간초과 조심..

for _ in range(10):
    ts = int(input())
    arr = [list(input()) for _ in range(100)]
    arr2 = list(zip(*arr)) #전치행렬
    ans = 0

    a = check(arr)
    b = check(arr2)

    if a >= b : ans = a
    else: ans = b

    print(f'#{ts}', ans)