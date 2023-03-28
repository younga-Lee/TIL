T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) #컨테이너 수, 트럭 수(트럭 당 한개의 컨테이너 수)
    w = list(map(int, input().split())) #화물의 무게
    t = list(map(int, input().split())) #트럭의 적재 용량
    total = 0 #옮겨진 화물의 전체무게

    #적재 용량이 큰 것 = 화물의 무게가 큰 것
    w.sort(reverse=True)
    t.sort(reverse=True)

    for i in range(M):
        for j in range(N):
            if t[i] >= w[j]:
                total += w[j]
                t[i] -= w[j]
                w[j] = 101
                break

        # # [2] 하나씩 짐 내리면서 현재 트럭에 가능한지 체크
        # i = ans = 0
        # for n in lst1:
        #     if n <= lst2[i]:  # 현재 트럭에 적재가능
        #         ans += n  # 누적
        #         i += 1  # 다음트럭
        #         if i == M:
        #             break

    print(f'#{tc} {total}')