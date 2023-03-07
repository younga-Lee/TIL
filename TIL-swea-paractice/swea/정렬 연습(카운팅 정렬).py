import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for ts in range(1, T+1):
    N = int(input())  # lst의 개수
    lst = list(map(int, input().split()))
    temp = [0] *N

    #lst중에 최대값찾기
    mx = lst[0]
    for _ in lst[0:]: #버블정렬 -> lst중 최대값찾기,, max가능하다면 굳이 이렇게 안해도 될듯
        if mx < _:
            mx = _
    #count배열
    count = [0]*(mx+1) #lst의 최대값(+1) 만큼 메모리할당 : 인덱스가 아니라 숫자로 들어있기 때문
    for i in range(len(lst)):
        count[lst[i]] += 1

    #count 재배열
    for c in range(1,len(count)):
        count[c] += count[c-1]

    #배열 및 확인
    for j in range(N-1, -1, -1): #뒤에서부터 하나씩
        count[lst[j]] -= 1 #카운트 배열에서 하나씩 삭제
        temp[count[lst[j]]] = lst[j]
    print(f'#{ts}', *temp)