import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for ts in range(1, T+1):
    N = int(input())
    A = int(input())

    count = [0]*(11) #카운트세기
    for a in range(len(str(A))):
        count[A%10] += 1
        A //= 10

    mx = count[0] #최대값구하기
    for c in range(len(count)):
        if count[c] > mx:
            mx = count[c]
    num = 0
    for c in range(len(count)):
        if count[c] == mx:
            num = c

    print(f'#{ts} {num} {mx}')
