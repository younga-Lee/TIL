import sys
sys.stdin = open("s_input.txt", "r")
#K,N,M = 한번 충전으로 이동할 수 있는 수 /전체정류장 개수 / 충전기 설치된 정류장 개수
T = int(input())

for ts in range(1,T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split())) #충전기 있는 버스정류장 번호

    count = [0] *(N+1) #전체정류당 갯수 + 1만큼 공간 할당 (인덱스랑 숫자가 다르기 때문)
    cnt = 0 #충전횟수
    f = 0 # 예비 위치
    while True:
        f += K #현재위치에서 이동할 수 있는 만큼 이동
        if f >= N : break #전체정류장 이상이면 loop문 멈춤
        else:
            cnt += 1
            for i in range(K): #0,1,2,...,K-1 순으로 차이 찾아보기
                if f-i in charge: #가장 가까운 충전소에 들리자.
                    f = f-i 
                    break
            else:
                cnt = 0 #충전소에 들릴 수 없는 상황
                break

    print(f'#{ts} {cnt}')



