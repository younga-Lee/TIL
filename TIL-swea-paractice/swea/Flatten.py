# 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램

import sys
sys.stdin = open("s_input.txt", "r")

for ts in range(1, 11):
    N = int(input()) #덤프 횟수
    hs = list(map(int, input().split())) #hs의 길이는 100

    # # N번 반복가능
    # #가장 높은 막대를 고르기
    # #가장 높은 막대를 -1하고, 가장 작은 막대값을 +1
    # 
    # for n in range(N):
    #     hs[hs.index(max(hs))] -= 1
    #     hs[hs.index(min(hs))] += 1
    # 
    # #바뀐 hs중에 가장 큰 값 - 가장 작은 값
    # 
    # print(f'#{ts} {max(hs)-min(hs)}')

    #max안쓴 버전
    def find_mx(hs):
        mx = 0
        for i in range(100):
            if mx < hs[i]:  # 최대값
                mx = hs[i]
                mx_index = i
        return mx_index


    def find_mn(hs):
        mn = 100
        for i in range(100):
            if mn > hs[i]:  # 최소값
                mn = hs[i]
                mn_index = i
        return mn_index

    for n in range(N):
        hs[find_mx(hs)] -= 1
        hs[find_mn(hs)] += 1

    print(f'#{ts} {hs[find_mx(hs)]-hs[find_mn(hs)]}')
