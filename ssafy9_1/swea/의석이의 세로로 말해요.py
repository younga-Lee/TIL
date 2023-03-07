import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    arr = []
    mx_len = 0
    #최대길이 찾기, 값입력 받기
    for _ in range(5):
        w = input()
        arr.append(list(w))
        if mx_len < len(w):
            mx_len = len(w)

    #''리스트에 값 넣기
    lst = [['']*mx_len for _ in range(5)]
    for i in range(5):
        for j in range(len(arr[i])):
            lst[i][j] = arr[i][j]


    ans = ''
    for li in range(mx_len):
        for lj in range(5):
            if lst[lj][li] != '':
                ans += lst[lj][li]
            else:
                continue
    print(f'#{tc} {ans}')