T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[1]) #종료순으로 활동 정렬

    a = [arr[0]] #선택된 활동들

    j = 1
    while j != len(arr):
        if a[-1][1] > arr[j][0]:
            arr.remove(arr[j])
        else:
            a.append(arr[j])
            j += 1

    print(f'#{tc} {len(a)}')