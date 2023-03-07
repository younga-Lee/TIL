import sys
sys.stdin = open("input1.txt", "r")
#0과1 로 이루어진 수열에서 연속한 1의 개수 중 최대값 출력

T = int(input())

for ts in range(1, T+1):
    N = int(input()) #수열의 길이
    arr = input() #수열

    mx = ans = 0
    for n in range(N):
        if arr[n] == '1': ans += 1 #수열중 1인 숫자가 있으면 ans에 1을 더하기
        else: ans = 0 #수열중 0이라면 ans초기화
        if mx < ans: mx = ans #ans중 최대값 구하기
    print(f'#{ts} {mx}')
