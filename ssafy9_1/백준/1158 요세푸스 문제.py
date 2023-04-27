from collections import deque
N, K = map(int, input().split())
q = deque(list(range(1, N+1)))
ans = []
while q:
    for i in range(K-1):
        q.append(q.popleft())
    ans.append(q.popleft())

result = "<" + ", ".join(str(x) for x in ans) + ">"
print(result)