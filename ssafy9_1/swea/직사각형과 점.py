import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())

    case1 = []
    case2 = []
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if i == x1 or i == x2 or j == y1 or j == y2:
                case1.append((i, j))
            else:
                case2.append((i, j))

    cnt1 = cnt2 = cnt3 = 0
    for _ in range(N):
        c = tuple(map(int, input().split()))
        if c in case1:
            cnt1 += 1
        elif c in case2:
            cnt2 += 1
        else:
            cnt3 += 1


    print(f'#{tc}', cnt2, cnt1, cnt3)