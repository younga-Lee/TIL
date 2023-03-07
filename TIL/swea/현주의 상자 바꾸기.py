import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for ts in range(1, T+1) :
    N, Q = map(int, input().split())

    N = [0] * (N+1)
    for i in range(1,Q+1): #변경할 숫자는 i
        L, R = map(int, input().split())
        for j in range(L, R+1) : #L~R까지를 i로 바꾸기
            N[j] = i

    print(f'#{ts}', *N[1:])
