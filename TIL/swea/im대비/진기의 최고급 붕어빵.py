import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split()) #예약한 사람수, 붕어빵 만드는 소요 시간, 붕어빵 개수(M시간당)
    time = sorted(list(map(int, input().split()))) #각사람이 도착하는 시간
    count = [0] * 11112
    ans = 'Possible'

    for i in range(M, len(count)):
        count[i] = i//M * K
    for t in range(N):
        if count[time[t]] < t+1:
            ans = 'Impossible'
            break
    print(f'#{tc} {ans}')