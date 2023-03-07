import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for ts in range(1, T+1):
    N, M = map(int, input().split()) #정수개수, 구간개수
    arr = list(map(int, input().split())) #N개의 정수

    maxV = 0
    minV = 1000000
    for i in range(N-M+1):
        total = 0
        for j in range(i, i+M): #M의 개수만큼 더하기
            total += arr[j]
        if total > maxV:
            maxV = total
        if total < minV:
            minV = total

    print(f'#{ts} {maxV-minV}')


#sol2
# for ts in range(1, T+1):
#     N, M = map(int, input().split()) #정수개수, 구간개수
#     arr = list(map(int, input().split())) #N개의 정수
#
#     maxV = 0
#     minV = 1000000

    total = 0
    for i range(M):
        total += arr[i]

#     for i in range(N-M+1):
#         total = 0
#         for j in range(i, i+M): #M의 개수만큼 더하기
#             total += arr[j]
#         if total > maxV:
#             maxV = total
#         if total < minV:
#             minV = total
#
#     print(f'#{ts} {maxV-minV}')