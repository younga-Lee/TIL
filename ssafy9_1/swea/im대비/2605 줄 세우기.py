n = int(input())
num = [0] + list(map(int, input().split()))

lst = [1]
for i in range(2, n+1):
    lst.insert(i-num[i]-1, i)
print(*lst)
