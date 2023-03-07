import sys
sys.stdin = open("ex.txt", "r")

N = int(input())
#막대 리스트 만들기
lst = [list(map(int, input().split())) for n in range(N)]
lst = sorted(lst)

total = 0
mh = lst[0][1]
real_mh = max(lst, key=lambda x: x[1])

#꼭대기까지는 차근차근 올라가기
for i in range(1, lst.index(real_mh)+1): #lst의 한줄씩
    for _ in range(lst[i-1][0], lst[i][0]): #한칸씩
        if mh < lst[i-1][1]:
            mh = lst[i-1][1]
        total += mh
#꼭대기
total += real_mh[1] #total 42

#맨끝에서부터 꼭대기까지 올라오기
nh = lst[-1][1] #맨 마지막 막대 높이
for i in range(len(lst)-1, lst.index(real_mh), -1): #lst의 한줄씩
    for _ in range(lst[i][0], lst[i-1][0], -1): #한칸씩
        if nh < lst[i][1]:
            nh = lst[i][1]
        total += nh

print(total)
