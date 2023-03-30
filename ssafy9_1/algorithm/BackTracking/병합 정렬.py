def msort(lst):
    global ans
    if len(lst) < 2: #종료조건
        return lst

    #정렬
    m = len(lst) // 2
    left = msort(lst[:m])
    right = msort(lst[m:])

    # 오른쪽이 먼저 들어갈 경우
    if left[-1] > right[-1]:
        ans += 1

    # merge
    ret = [] #정렬될 리스트
    l = r = 0
    while l < len(left) and r < len(right):  # 비교할 대상 숫자가 있는경우 반복처리
        if left[l] < right[r]:  # left에 있는 값이 작은 경우
            ret.append(left[l])
            l += 1
        else:
            ret.append(right[r])
            r += 1
    ret += left[l:] + right[r:]  # 남은 값을 모두 뒤에 붙임 (left와 right 둘 중 하나는 빈 리스트)
    return ret


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    ans = 0
    lst = msort(lst)
    print(f'#{tc} {lst[N // 2]} {ans}')