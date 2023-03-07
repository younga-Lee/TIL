#N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

T = int(input()) #테스트 케이스

for ts in range(1, T+1):
    N = int(input())  # 양수의 개수
    arr = list(map(int, input().split())) #각 숫자들을 리스트로 변경

    maxV = arr[0] #가장 첫번째가  max라고 가정
    minV = arr[0] #가장 첫번째가  max라고 가정
    for i in range(1,N):
        if maxV < arr[i]:
            maxV = arr[i]
        elif minV > arr[i] :
            minV = arr[i]
    print(f'#{ts} {maxV-minV}')

