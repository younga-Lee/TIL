import sys
sys.stdin = open("a.txt", "r")

T = int(input())

for ts in range(1, T + 1):
    A, B = input().split()

    A = [a for a in A]
    cnt = 0
    for i in range(len(A)-len(B)+1):
        for j in range(len(B)):
            if A[i+j] != B[j]:
                break
        else:
            for j in range(len(B)): #만약 B단어가 들어가 있다면 그 문자열을 모두 ?로 바꾸기 (문자열 중복 제거)
                A[i+j] = '?'
            cnt += 1

    ans = (len(B) - 1) * cnt

    print(f'#{ts}', len(A) - ans)


#-- 문자열 제거때문에 한참걸림 ㅠㅜ