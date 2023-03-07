#버스 정류장 1~5000번
#버스 노선 N개
# 1번째 버스 노선은 번호1~3 모든 정류장을 다님
# 2번째 버스 노선은 번호2~5인 모든 정류장을 다님
# 구하는 것 : P 버스 정류장에 대해 각 정류장에 몇개의 버스 노선이 다니는지
# j는 C번 버스 정류장을 지나는 버스노선의 개수
import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for ts in range(1, T + 1):
    bs = [0] * 5001  # 버스 정류장
    N = int(input())  # 버스 노선 가져오기

    for i in range(N):  # 각 버스 노선의 정류장 지나는 것을 리스트로
        A, B = map(int, input().split())
        for j in range(A, B + 1):
            bs[j] += 1

    # P 버스 정류장에 대해 각 정류장에 몇개의 버스 노선이 다니는지
    c = []
    P = int(input())
    for p in range(1, P + 1):
        C = int(input())
        c.append(bs[p])

    print(f'#{ts}', *c)
