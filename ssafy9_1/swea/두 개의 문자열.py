import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for ts in range(1, T+1) :
    N, M = map(int, input().split())
    a_lst = list(map(int, input().split())) #a_lst길이는 N
    b_lst = list(map(int, input().split())) #b_lst길이는 M

    #순서 고정
    if M < N :
        N, M = M, N
        a_lst, b_lst = b_lst, a_lst

    ans = []
    for _ in range(M-N+1): #두 리스트 길이의 차만큼 반복
        total = 0
        for i in range(N): #작은 리스트를 기준으로 행렬곱
            total += (a_lst[i] * b_lst[i])
        ans.append(total) #결과값 ans리스에 저장
        b_lst.remove(b_lst[0]) #큰 리스중에 첫번째 값 제거 -> 리스트를 하나씩 밀기위함
    print(f'#{ts} {max(ans)}')
