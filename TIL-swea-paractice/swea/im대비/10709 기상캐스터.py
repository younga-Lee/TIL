H, W = map(int, input().split())
sky = [input() for _ in range(H)]
arr = [[-1]*W for _ in range(H)]

cnt = 0
for i in range(H):
    for j in range(W):
        if sky[i][j] == 'c':
            arr[i][j] = 0
            cnt = 0
        else:
            if arr[i][j-1] != -1:
                cnt += 1
                arr[i][j] = cnt
for h in range(H):
    print(*arr[h])