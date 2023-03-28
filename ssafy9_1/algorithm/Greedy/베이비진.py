def check(cnt):
    for i in range(12):
        if cnt[i] >= 3:  # triplet
            cnt[i] -= 3
            return False

        if cnt[i] >= 1 and cnt[i + 1] >= 1 and cnt[i + 2] >= 1:  # run
            cnt[i] -= 1
            cnt[i + 1] -= 1
            cnt[i + 2] -= 1
            return False
    return True

T = int(input())

for tc in range(1, T+1):
    cnt1, cnt2 = [0]*12, [0]*12
    lst = list(map(int, input().split()))
    ans = 0

    i = 0
    while i != len(lst):
        cnt1[lst[i]] += 1
        if check(cnt1) is False:
            ans = 1
            break
        else:
            i += 1

        cnt2[lst[i]] += 1
        if check(cnt2) is False:
            ans = 2
            break
        else:
            i += 1

    print(f'#{tc} {ans}')