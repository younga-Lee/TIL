#중위순회
def inorder_traverse(n):
	if n:
		inorder_traverse(ch1[n])
		node.append(n)
		inorder_traverse(ch2[n])

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    for i in range(2, N+1):
        if i%2:
            ch2[i//2] = i
        else:
            ch1[i//2] = i

    node = []
    inorder_traverse(1)

    print(f'#{tc}',node.index(1)+1, node.index(N//2)+1)