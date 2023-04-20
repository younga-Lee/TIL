def dfs(n, sm):
    if n == N:
        lst.add(sm)
        return
    dfs(n+1, sm+num[n])
    dfs(n+1, sm)

N = int(input())
num = list(map(int, input().split()))
lst = set()
dfs(0, 0)
lst = sorted(lst)
top = lst[-1]
for i in range(top):
    if i != lst[i]:
        print(i)
        break
else:
    print(top+1)