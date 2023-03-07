def inorder_traverse(n):
    if n:
        inorder_traverse(ch1[n]) #왼
        node.append(n)
        inorder_traverse(ch2[n]) #오

for tc in range(1, 11):
    N = int(input())

    #저장
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    word = dict()
    for _ in range(N):
        lst = list(input().split())
        word[int(lst[0])] = lst[1]
        if len(lst) == 4:
            ch1[int(lst[0])] = int(lst[2])
            ch2[int(lst[0])] = int(lst[3])
        if len(lst) == 3:
            ch1[int(lst[0])] = int(lst[2])

    node = []
    inorder_traverse(1)

    lst = []
    for i in node:
        lst.append(word[i])

    print(node)
    print(f"#{tc}",''.join(lst))
