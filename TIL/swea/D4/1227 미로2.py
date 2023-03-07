import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input())) for _ in range(100)]
    visited = [[0]*100 for _ in range(100)]
    ans = 0

    # 출발점 찾기
    for s in range(100):
        for e in range(100):
            if arr[s][e] == 2:
                si, sj = s, e
                break

    q = [(si, sj)]
    visited[si][sj] = 1

    while q:
        i, j = q.pop(0)
        for ri, rj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ni, nj = i+ri, j+rj
            if 0 <= ni < 100 and 0 <= nj < 100 and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni, nj))
                visited[ni][nj] = 1
                if arr[ni][nj] == 3:
                    ans = 1
                    break

    print(f'#{t} {ans}')