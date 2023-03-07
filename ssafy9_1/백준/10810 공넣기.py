N,M = map(int, input().split())

lst = [0]*N

for i in range(M):
    x, y, z = map(int, input().split())
    for j in range(x-1, y):
        lst[j] = z
print(*lst)
