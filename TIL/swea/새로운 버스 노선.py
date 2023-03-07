T = int(input())
for ts in range(1, T + 1):
    N = int(input())
    count = [0] * 1001
    for n in range(N):
        bus, A, B = map(int, input().split())
        if bus == 1:  # 일반
            for i in range(A, B + 1):
                count[i] += 1
        elif bus == 2:  # 급행
            for i in range(A, B + 1, 2):
                count[i] += 1
        elif bus == 3:  # 광역 급행
            if A % 2 == 0:
                for i in range(A, B + 1):
                    if i % 4 == 0: count[i] += 1
            else:
                for i in range(A, B + 1):
                    if (i % 3 == 0) and (i % 10 != 0): count[i] += 1

    print(f'#{ts} {max(count)}')

#count 1추가 안해서 틀린거 실화임? 원래 바로 짰는데 ㅠㅠ이거때매 40분 더 걸렸어 으악!