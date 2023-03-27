T = int(input())

for tc in range(1, T+1):
    num = list(map(int,list(input())))
    num.sort()
    ans = 1

    for i in [0, 3]:
        if num[i] == num[i+1] == num[i+2] : #triplet
            pass
        elif num[i] == num[i+1]-1 and num[i+2] == num[i+1]+1: #run
            pass
        else:
            ans = 0
            break

    print(f'#{tc} {ans}')