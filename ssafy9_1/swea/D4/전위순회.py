def preord(n):
    if n:  # 존재하는 노드라면 처리
        alst.append(n)  # 방문: 필요한 처리
        preord(ch1[n])  # 왼쪽 노드
        preord(ch2[n])  # 오른쪽 노드


T = int(input())
for tc in range(1, T + 1):
    V = int(input())
    lst = list(map(int, input().split()))
    # [1] 트리구조를 저장(일반트리=>left/right: 자식노드 저장)
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    for i in range(0, len(lst), 2):
        p, c = lst[i], lst[i + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    alst = []
    preord(1)
    print(f'#{tc}', *alst)
