w, h = map(int, input().split()) #가로 세로
p, q = map(int, input().split()) #개미의 가로, 세로 위치
t = int(input()) #움직일 시간

dr = [(-1, 1), (1, 1)]
while t > 0:
    for di, dj in dr:
        ni, nj = p + di, q + dj
        if 0 <= ni < w and 0 <= nj < h:
            t -= 1
            p, q = ni, nj
    else:
        break
print(p,q)