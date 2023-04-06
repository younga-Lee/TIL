N = int(input()) #시험장 개수
A = list(map(int, input().split())) #각 시험장에 있는 응시자의 수
B, C = map(int, input().split()) #총감독관(1명)이 감시할수 있는 응시자수, 부감독관
cnt = 0
for i in range(N):
    A[i] -= B
    cnt += 1
    if A[i] <= 0:
        pass
    else:
        if A[i]%C == 0:
            cnt += A[i]//C
        else:
            cnt += A[i]//C + 1

print(cnt)