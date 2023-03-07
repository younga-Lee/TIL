T = int(input())

for ts in range(1, T+1):
    arr = list(map(int, input().split()))
    ans = 0

    for i in range(1<<10) :
        for j in range(10):
            if i & (1<<j) :
                print(arr[j], end = ' ')


    #비트 쓰는 이유 -> 가능한 모든 집합을 보기 위해서서
