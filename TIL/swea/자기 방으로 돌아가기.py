import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [0] * 401

    for _ in range(N):
        a, b = map(int, input().split())
        if a> b:
            a, b = b, a
        if a%2:
            if b%2: #홀홀
                for i in range(a, b + 2):
                    arr[i] += 1
            else: #홀짝
                for i in range(a, b+1):
                    arr[i] += 1
        else:
            if b % 2:  #짝홀
                for i in range(a - 1, b + 2):
                    arr[i] += 1
            else:  #짝짝
                for i in range(a - 1, b + 1):
                    arr[i] += 1

    print(f'#{tc} {max(arr)}')
