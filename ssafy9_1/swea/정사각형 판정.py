import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = 'yes'

    #  [1] '#'전체를 감싸는 범위: 좌측상단:(si,sj),우측하단:(ei,ej) 좌표 구하기
    si, sj, ei, ej = N, N, 0, 0  # 초기값: 무조건 갱신되는 값으로 초기화(mx: 최소값으로)
    for i in range(N):
        for j in range(N):  # '#'일때 최소/최대 좌표 갱신
            if arr[i][j] == '#':
                if si > i:    si = i
                if sj > j:    sj = j
                if ei < i:    ei = i
                if ej < j:    ej = j

    # [2] 판정
    if (ei - si) != (ej - sj):  # 가로!=세로
        ans = 'no'
    else:
        for i in range(si, ei + 1):  # 좌상~우하 전체 # 이어야함
            for j in range(sj, ej + 1):
                if arr[i][j] != '#':
                    ans = 'no'
                    break
            if ans == 'no':
                break

    print(f'#{test_case} {ans}')