# 1주일에 L분 이상 U분 이하의 운동
#이번 주에 X분만큼
# 제한되어 있는 시간을 넘은 운동을 한 것인지,
# 그것이 아니라면 몇 분 더 운동을 해야 제한을 맞출 수 있는지 출력하는 프로그램
#필요한 양보다 더 많은 운동을 하고 있다면 -1
#아니라면 추가로 몇 분을 더 운동해야 하는지

T = int(input())

for ts in range(1, T+1):
    L, U, X = map(int, input().split())
    if X >= U: ans = -1
    elif X <= L: ans = L-X
    else: ans = 0

    print(f'#{ts} {ans}')

#--또 쉬움--