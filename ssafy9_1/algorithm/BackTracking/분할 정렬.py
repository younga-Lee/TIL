def msort(s, e):
    if s == e:
        return
    m = (s+e)//2
    msort(s, m) #왼쪽
    msort(m+1, e) #오른쪽

    #merge
    k = 0
    l, r = s, m+1 #왼쪽과 오른쪽에서 가장 작은 숫자의 위치
    while l <= m or r <= e:
        if l <= m and r <= e:
            if arr[l] <= arr[r]: #더 작은 것 복사
                tmp[k] = arr[l]
                l += 1
            else:
                tmp[k] = arr[r]
                r += 1
            k += 1
        elif l <= m : #왼쪽만 남았을 때
            while l <= m:
                tmp[k] = arr[l]
                l += 1
                k += 1
        elif r <= e : #오른쪽만 남았을 때
            tmp[k] = arr[r]
            r += 1
            k += 1

    #tmp에 있던거 arr에 덮어쓰기기
    i = 0
    while i < k :
        arr[s+i] = tmp[i]
        i += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0]*N #정렬된 리스트
    msort(0, N-1)
    print(arr)