T = int(input()) #지도의 개수

for tc in range(1, T+1):
    N = int(input()) #지도크기 NxN
    hi = [list(map(int,input().split())) for _ in range(N)]
    ans = -1 #봉우리가 없거나 1개 일때는 -1출력
    dr = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]  # 델타 8가지 위치
    bongwori = [] #봉우리들

    # 봉우리 = 주변 8개 구역보다 높으면 봉우리
    for i in range(1, N-1):
        for j in range(1, N-1):
            mx = 0
            for r in dr:
                if hi[i][j] > hi[i+r[0]][j+r[1]]: #가운데와 그 주위방향 비교
                    mx = hi[i][j]
                else: #봉우리가 아닌경우
                    break
            if mx != 0:
                bongwori.append(mx) #봉우리들
                
    #가장 높은 봉우리와 가장 낮은 봉우리의 높이 차이
    mx, mn = 0, 10000000
    if len(bongwori) > 1:
        for b in bongwori:
            if b > mx:
                mx = b
            if b < mn:
                mn = b
        ans = mx - mn
    print(f'#{tc} {ans}')