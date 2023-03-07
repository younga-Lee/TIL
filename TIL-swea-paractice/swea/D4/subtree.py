def check(n):
    if n:
        node.append(n)
        check(ch1[n])
        check(ch2[n])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split()) #간선의 개수, 노드트리 번호
    lst = list(map(int, input().split()))

    #간선 저장
    V = max(lst)
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    for i in range(0, len(lst), 2):
        p, c = lst[i], lst[i + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    node = []
    check(N)
    print(f'#{tc}', node)