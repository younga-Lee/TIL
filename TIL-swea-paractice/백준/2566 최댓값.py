arr = [list(map(int, input().split())) for _ in range(9)]

mx , mxrow, mxcol = 0, 0, 0
for i in range(9):
    if max(arr[i]) > mx :
        mx = max(arr[i])
        mxrow = i
        mxcol = arr[i].index(mx)

print(mx)
print(mxrow+1, mxcol+1)