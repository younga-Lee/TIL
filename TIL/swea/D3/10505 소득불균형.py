#n명의 사람의 소득이 주어졌을 때 이 중 평균 이하의 소득을 가진 사람들의 수를 출력

T = int(input())

for ts in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans =0
    for i in lst:
        if i <= sum(lst)/N:
            ans += 1

    print(f'#{ts} {ans}')
    
#쉬움