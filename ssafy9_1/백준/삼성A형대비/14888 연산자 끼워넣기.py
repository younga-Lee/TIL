def dfs(n, sm):
    global mx, mn
    if n == N:
        mx = max(mx, sm)
        mn = min(mn, sm)
        return
    for j in range(4):
        if sig[j] >= 1:
            sig[j] -= 1
            if j == 0:
                dfs(n+1, sm+nums[n])
            elif j == 1:
                dfs(n+1, sm-nums[n])
            elif j == 2:
                dfs(n+1, sm*nums[n])
            else:
                if sm >= 0:
                    dfs(n+1, sm//nums[n])
                else: #음일 때
                    dfs(n+1, -(abs(sm)//nums[n]))
            sig[j] += 1
N = int(input()) #숫자 수
nums = list(map(int, input().split()))
sig = list(map(int, input().split())) # + - x *
mx, mn = -1000000000, 1000000000 #기본값 문제 보고 잘 결정하기
dfs(1, nums[0])
print(mx)
print(mn)