T = int(input())
for _ in range(T):
    N, M = map(int, input().split()) #문서의 개수, 몇 번째로 인쇄되었는지 궁금
    power = list(map(int, input().split())) #숫자가 높을 수록 먼저
    q = list(range(N))
    lst = [] #인쇄할 것

    print(lst[M]+1)