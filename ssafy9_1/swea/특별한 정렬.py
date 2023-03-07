import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for ts in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1):
        mx = i
        mn = i
        for j in range(i+1, N):
            if i%2 == 0 :#짝수일때가 큰값 내림차순
                if arr[mx] < arr[j]:
                    arr[mx], arr[j] = arr[j], arr[mx]
            else:#홀수일때가 작은값 오름차순
                if arr[mn] > arr[j]:
                    arr[mn], arr[j] = arr[j], arr[mn]

    print(f'#{ts}', *arr[:10])