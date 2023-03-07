T = int(input())
A = {1,2,3,4,5,6,7,8,9,10,11,12}
for ts in range(1, T+1):
    K, N = map(int, input().split())
    for i in range(1<<12):
        for