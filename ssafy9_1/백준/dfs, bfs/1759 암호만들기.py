def dfs(n, cnt, lst):
    if cnt > L: #가지치기
        return

    if n == C:
        if cnt == L:
            a = 0 #모음
            b = 0 #자음
            for i in range(len(lst)):
                if lst[i] in ['a','e','o','i','u']:
                    a += 1
                else:
                    b += 1

            if a >= 1 and b >= 2:
                print(''.join(lst))
        return
    dfs(n+1, cnt+1, lst+[num[n]]) #골랐을 때
    dfs(n+1, cnt, lst) #안골랐을 때

L, C = map(int, input().split()) #암호길이, 주어진 숫자개수
num = sorted(input().split())
dfs(0, 0, [])

