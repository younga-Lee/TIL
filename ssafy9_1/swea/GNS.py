import sys
sys.stdin = open("s_input.txt", "r")

num = {"ZRO" : 0 , "ONE": 1, "TWO" : 2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}

T = int(input())
for ts in range(1, T+1):
    t, N = input().split()
    N = int(N)
    lst = input().split()

    #문자를 숫자로 바꿔주기
    num_lst = []
    for i in lst:
        for k, v in num.items():
            if i == k:
                num_lst.append(num[k])

    #정렬 후, 숫자를 문자로 바꿔주기
    num_lst = sorted(num_lst)
    str_lst = []
    for n in num_lst:
        for k, v in num.items():
            if n == num[k]:
                str_lst.append(k)
    print(f'#{ts}')
    print(*str_lst)
