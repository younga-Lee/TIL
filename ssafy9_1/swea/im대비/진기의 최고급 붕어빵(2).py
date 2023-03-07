import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split()) #예약한 사람수, 붕어빵 만드는 소요 시간, 붕어빵 개수(M시간당)
    time = sorted(list(map(int, input().split()))) #각사람이 도착하는 시간
    count = [0] * 11,112
    ans = 'Possible'

    for t in time:
        if t < M:
            ans = 'Impossible'
            break
        else:
            for i in range(1, M * K + 1):
                count[i] += K
                if i % M == 0:
                    K += K

            # for j in range(t-1, len(count)):
            #     count[j] -= 1

    print(f'#{tc} {ans}')