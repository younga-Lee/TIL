def dfs(n, cnt, lst):
    if n == N:
        if cnt == 6 : #로또 번호는 6개
            print(*lst)
        return
    dfs(n+1, cnt+1, lst+[num[n]])
    dfs(n+1, cnt, lst)

while True:
    lotto = list(map(int,input().split()))
    if lotto[0] == 0:
        break
    N = lotto[0]
    num = lotto[1:]
    dfs(0, 0, [])
    print()
