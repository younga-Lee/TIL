import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split()) #노드의 개수, 리프노드의 개수, 값을 출력할 노드 번호
    heap = list(range(N+1))
    val = [0]*(N+1)

    #기본값 저장
    for _ in range(M):
        a, b = map(int, input().split())
        val[a] = b

    #노드번호
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    for i in range(2, N+1):
        if i%2:
            ch2[i//2] = i
        else:
            ch1[i//2] = i

    #값 연산
    for h in heap[::-1]:
        if ch1[h] or ch2[h]:
            val[h] = val[ch1[h]] + val[ch2[h]]

    print(f'#{tc} {val[L]}')
