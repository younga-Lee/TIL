N = int(input())
arr = list(map(int, input().split()))

mx = 1
mn = 1
ans = 1
for i in range(N-1):
    if arr[i] <= arr[i+1]: #커질때
        mx += 1
    else:
        if ans < mx:
            ans = mx
        mx = 1

    if arr[i] >= arr[i+1]: #작아질때
        mn += 1
    else:
        if ans < mn:
            ans = mn
        mn = 1
if ans < mn:
    ans = mn
if ans < mx:
    ans = mx

print(ans)