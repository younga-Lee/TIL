import sys
sys.stdin = open("s_input.txt", "r")

for ts in range(1,4): #추후 11로 수정할 것.
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 0
    for i in range(2, N-2): #양옆끝빼고 건물 하나씩
        m = 100000
        d1 = lst[i] - lst[i - 2]
        d2 = lst[i] - lst[i - 1]
        d3 = lst[i] - lst[i + 1]
        d4 = lst[i] - lst[i + 2]
        if d1>0 and d2>0 and d3>0 and  d4 > 0:
            if d1 < m :
                m = d1
            if d2 < m:
                m = d1
            if d3 < m :
                m = d1
            if d4 < m :
                m = d1
                cnt += m
    print(f'#{ts} {cnt}')
