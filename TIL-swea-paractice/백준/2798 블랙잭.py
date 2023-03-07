N, M = map(int, input().split()) #카드의 개수, 합
lst = list(map(int, input().split()))

ans = []
for i in range(N-1, -1, -1):
    for j in range(i):
        for k in range(j):
            if lst[i]+lst[j]+lst[k] <= M:
                ans.append(lst[i]+lst[j]+lst[k])
print(max(ans))