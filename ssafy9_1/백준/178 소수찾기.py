N = int(input())
num = list(map(int, input().split()))

cnt = len(num)
for n in num:
    if n > 2:
        for i in range(2, n):
            if n%i == 0: #소수가 아니라면
                cnt -= 1
                break
    elif n ==2:# 2일 경우 생각하기!
        pass
    else:
        cnt -=1
print(cnt)