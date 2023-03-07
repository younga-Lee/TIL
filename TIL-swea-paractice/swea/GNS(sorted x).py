import sys
sys.stdin = open("s_input.txt", "r")

num = {"ZRO" : 0 , "ONE": 1, "TWO" : 2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}

T = int(input())
for ts in range(1, T+1):
    t, N = input().split()
    N = int(N)
    lst = input().split()

    #버블 정렬
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if num[lst[j]] > num[lst[j+1]]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    print(f'#{ts}')
    print(*lst)