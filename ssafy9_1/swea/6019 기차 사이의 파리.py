import sys

sys.stdin = open("s_input.txt", "r")

# D는 두 기차 전면부 사이의 거리, A는 기차 A의 속력, B는 기차 B의 속력, F는 파리의 속력

T = int(input())
for ts in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    time = D/(A+B) #A, B가 마주칠때까지 걸린 시간
    print(f'#{ts} {time*F}')