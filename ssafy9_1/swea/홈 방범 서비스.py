#마름모는 N//2+1
import sys
sys.stdin = open("sample_input.txt", "r")

def check(i, j): #십자가 형태로 보기
    a = []
    dr = [(0,0), (0,1), (0,-1), (1,0), (-1,0)]

    for k in range(K):
        i, j = i+k, j
        si, sj
        for di, dj in dr:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
                a.append((ni, nj))
    return a

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) #도시의 크기, 집이 내는 돈
    arr = [[0]*(N//2)+list(map(int, input().split())) for _ in range(N)]

    ans = []
    K = 1
    for i in range(N):
        for j in range(N):
            while K*K+(K-1)*(K-1) <= M*len(set(ans)) : #손해보지 않을 때까지
                K += 1
            print(ans)