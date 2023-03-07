N = int(input())

lst = []
for id, e in enumerate(range(N)):
    a, b = input().split()
    a = int(a)
    lst.append((id, a, b))
s_lst = sorted(lst, key = lambda x: (x[1], x[0]))

for i in range(N):
    print(s_lst[i][1], s_lst[i][2])