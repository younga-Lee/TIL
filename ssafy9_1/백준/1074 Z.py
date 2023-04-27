def z(i, j):
    global cnt
    for di, dj in [(0,0),(0,1),(1,-1),(0,1)]:
        ni, nj = i+di, j+dj
        cnt += 1
        if ni==r-1 and nj==c-1:
            return True
    return False

N, r, c = map(int, input().split())
cnt = 0

print(cnt)