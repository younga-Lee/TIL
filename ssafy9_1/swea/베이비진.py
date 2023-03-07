import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for ts in range(1, T+1):
    num = int(input())

    #카운트
    count = [0]*12
    for i in range(len(str(num))):
        count[num%10] += 1
        num //= 10

    #triplet일때
    for t in range(len(count)):
        if count[t] >= 3:
            count[t] -=3

    #run일때
    for r in range(1,len(count)-1):
        if count[r-1] and count[r] and count[r+1] != 0:
            count[r-1] -= 1
            count[r] -= 1
            count[r+1] -= 1

    if count == [0]*12 :
        print(f'#{ts} 1')
    else:
        print(f'#{ts} 0')