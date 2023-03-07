T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) #도화지크기 NxN, 도장을 찍은 횟수
    ans = []
    for _ in range(M):
        x, y, l, h = map(int, input().split()) #왼쪽모서리좌표, 너비, 높이
        
        # 도장이 찍혀있는 곳에 대한 좌표 구하기
        lst = [] #도장이 찍혀있는 모든 곳에 대한 좌표
        for i in range(l):
            for j in range(h):
                lst.append((y+i, x+j))
        ans.extend(lst)

    print(f'#{tc}', len(set(ans))) #겹치지 않는 부분의 개수만 출력