import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #마지막 노드
    lst = [0]+list(map(int, input().split()))

    #이진노드 정렬
    while True:
        for i in range(1, N+1):
            c = i
            p = c//2
            while p > 0 and lst[p] > lst[c]:
                lst[p], lst[c] = lst[c], lst[p]
                c = p
                p = c//2
        else:
            break

    ans = 0
    c = N
    p = c//2
    while p:
        ans += lst[p]
        c = p
        p = c//2

    print(f'#{tc}', ans)
