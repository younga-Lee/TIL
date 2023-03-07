N, K = map(int, input().split()) #온도를 측정한 전체 날짜의 수/ 합을 구하기 위한 연속적인 날짜의 수
arr = list(map(int, input().split()))
ans = []

for i in range(N-K+1):
    total = 0
    for k in range(K):
        total += arr[i+k]
    ans.append(total)
print(max(ans))

#시간초과떠서 지렁이 처럼 해야댕