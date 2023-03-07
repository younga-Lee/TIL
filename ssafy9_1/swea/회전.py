import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) #숫자 수, 작업 수
    num = list(map(int, input().split()))

    for _ in range(M):
        num.append(num.pop(0))

    print(f'#{tc} {num[0]}')