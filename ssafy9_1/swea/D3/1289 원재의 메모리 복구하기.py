#초기상태는 0000
T = int(input())

for ts in range(1, T+1):
    origin = input()
    init = '0' * len(origin)
    cnt = 0


    for o in range(len(origin)):
        if origin[o] == '1' :
            init[o] == '1'
        print(init)
    print(f'#{ts} {cnt}')