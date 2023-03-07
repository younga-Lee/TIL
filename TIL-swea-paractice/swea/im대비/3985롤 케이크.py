L = int(input())
cnt = [0]*(L+1)
N = int(input())

mx = 0 #기대한 방청객
mx_idx = 0
for n in range(1, N+1):
    p, k = map(int, input().split())
    for i in range(p, k+1):
        if cnt[i] == 0: #케이크 조각 번호
            cnt[i] = n
        if mx < k-p: #기대
            mx = k-p
            mx_idx = n
print(mx_idx) #인덱스!

real_mx = 0
real_num = 0
for n in range(1, N+1):
    if real_mx < cnt.count(n):
        real_mx = cnt.count(n)
        real_num = n
print(real_num)

#쉽게 품
