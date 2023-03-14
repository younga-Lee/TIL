progresses = [1, 1, 50]
speeds = [100, 2, 1]

ans = []
num = []

N = len(progresses)
for i in range(N):
    if (100 - progresses[i]) % speeds[i] == 0:
        num.append((100 - progresses[i]) // speeds[i])
    else:
        num.append(((100 - progresses[i]) // speeds[i]) + 1)


ans = []

num.append(100)
n = 0
mx = 0
cnt = 1
while True:
    if num[mx] >= num[n + 1]:
        mx = n
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 1
        mx
    n += 1
    if n == N:
        break
print(ans)