import sys
sys.stdin = open("input.txt", "r")

#숫자하나라도 0 되면 종료
for _ in range(10):
    tc = int(input())

    arr = list(map(int, input().split()))   #8개로 되어있음

    i = 0
    num = [1, 2, 3, 4, 5]
    while arr[-1] > 0:
        arr.append(arr.pop(0)-num[i])
        i = (i + 1) % 5
    arr.pop()
    arr.append(0)
    print(f'#{tc}', *arr)