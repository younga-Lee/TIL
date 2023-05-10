from itertools import permutations
n = int(input())
k = int(input())
lst = [input() for _ in range(n)]
ans = []
for i in list(permutations(lst, k)):
    ans.append(''.join(i))
print(len(set(ans)))
