T = int(input())

for ts in range(1, T+1):
    A, B = map(int,input().split())
    print(f'#{ts} {(A+B)%24}')

#-- 너무.. 쉬운데? --