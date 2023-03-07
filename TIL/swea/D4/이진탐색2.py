def inord(n):
    global cnt
    if 1 <= n <= N:  # 노드가 존재하는 경우 처리
        inord(n * 2)  # left
        lst[n] = cnt  # 단위작업
        cnt += 1
        inord(n * 2 + 1)  # right


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [0] * (N + 1)
    # [1] inorder로 값을 저장
    cnt = 1
    inord(1)  # root부터 숫자 저장
    print(f'#{tc} {lst[1]} {lst[N // 2]}')