import sys
sys.stdin = open("s_input.txt", "r")

def nCr(n, r):
    n_lst = [a for a in range(n, 0, -1)][:r]
    r_lst = [b for b in range(1, r+1)]
    n_result = 1
    r_result = 1

    for i in n_lst:
        n_result *= i
    for j in r_lst:
        r_result *= j

    return int(n_result/r_result)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N = int(N/10)
    cnt = 0

    for i in range(1, N//2+1):
        cnt += nCr(N-i, i) * (2**i)

    print(f'#{tc} {cnt+1}') #i가 0일 경우

