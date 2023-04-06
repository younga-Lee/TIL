def dr(n):
    if n == 1:
        return (0, 1)
    if n == 2:
        return (0, -1)
    if n == 3:
        return (-1, 0)
    if n == 4:
        return (1, 0)

N, M, x, y, K = map(int, input().split()) #지도 세로, 가로크기, 주사위 좌표 x, y, 명령 개수
arr = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))

