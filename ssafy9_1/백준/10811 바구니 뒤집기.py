N,M = map(int, input().split())

lst = list(range(1, N+1))

for i in range(M):
    x, y = map(int, input().split())
    lst[x-1:y] = lst[x-1:y][::-1]
print(*lst)
