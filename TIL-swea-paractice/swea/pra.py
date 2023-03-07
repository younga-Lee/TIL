import sys
sys.stdin = open("algo2_sample_in.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input()) #두더지가 머리를 내미는 횟수
    r, c = map(int, input().split()) #망치의 시작위치
    score = 0

    for _ in range(N):
        A, B, K = map(int, input().split()) #두더지의 좌표(A,B), 고개를 내미는 시간(초)
        t = abs(r - A) + abs(c - B)  # 두더지를 때리기 위해 걸리는 시간
        if K >= t: #점수를 획득하는 경우
            score += 1
            r, c = A, B
        else: #점수를 획득하지 못할 경우(망치의 위치만 바뀐다)
            if abs(c - B) >= K:  #가로축만 이동할 경우
                if c <= B:
                    c += K
                else:
                    c -= K

            else: #가로축 이동 후, 세로축도 이동할 경우
                c = B
                K = K-abs(c - B)-1
                if r <= A:
                    r += K
                else:
                    r -= K

    print(f'#{tc} {score}')