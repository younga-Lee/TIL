import sys
sys.stdin = open("s_input.txt", "r")

C = int(input())

for tc in range(1, C+1):
    N, M = map(int, input().split())  #배열의 세로크기, 가로크기
    arr = [list(list(input())) for _ in range(N)]

    secret = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111':8, '0001011': 9}

    for i in range(N):
        if '1' in arr[i]: #행찾기
            for j in range(M-1, 55, -1): #56개 찾기
                if arr[i][j] == '1':
                    info = arr[i][j-55:j+1]
                    break

    #7개 묶기
    lst = []
    for k in range(0, 56, 7):
        num = ''
        num += ''.join(info[k:k+7])
        lst.append(secret[num])

    total = 0
    for l in range(len(lst)):
        if l%2:
            total += lst[l]
        else:
            total += 3*lst[l]
    if total%10 == 0:
        ans = sum(lst)
    else:
        ans = 0

    print(f'#{tc}', ans)





