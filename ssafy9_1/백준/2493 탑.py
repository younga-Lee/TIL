N = int(input())
stk = list(map(int, input().split()))
lst = []
for _ in range(N):
    top = stk.pop()
    for j in range(len(stk)-1, -1, -1):
        if stk[j] > top:
            lst.append(j+1)
            break
    else:
        lst.append(0)
ans = []
while lst:
    ans.append(lst.pop())
print(ans)
