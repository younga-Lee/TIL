N, M = map(int, input().split())

lst = list(range(1, N+1))

for i in lst:
    for j in lst:
        ans = []
        if i != j :
            print(i, j)