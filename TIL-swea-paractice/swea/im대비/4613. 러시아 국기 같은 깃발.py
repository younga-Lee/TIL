#T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(input()) for _ in range(N)]
#     lst = []
#
#     #줄마다 분포
#     for i in range(N):
#         cnt_dict = {'W': 0, 'B': 0, 'R': 0}
#         for j in range(M):
#             if arr[i][j] == 'W':
#                 cnt_dict['W'] += 1
#             elif arr[i][j] == 'B':
#                 cnt_dict['B'] += 1
#             elif arr[i][j] == 'R':
#                 cnt_dict['R'] += 1
#         lst.append(cnt_dict)
#
#     #B와 R부터 구해보기
#     col = ['R']
#     for i in range(N-2, 0, -1):
#         if lst[i]['B'] > lst[i]['R']:
#             col.append('B')
#             break
#         else:
#             col.append('R')
#
#     #W와 B부터 구해보기
#     if i == 1:
#         j = 1
#     else:
#         for j in range(i-1, 0, -1):
#             if lst[i]['W'] > lst[i]['B']:
#                 col.append('W')
#                 break
#             else:
#                 col.append('B')
#     #나머지 W하기
#     for k in range(j-1, -1, -1):
#         col.append('W')
#
#     #근데 만약 B들어갈 공간이 없으면?
#     if 'B' not in col:
#         col[1] = 'B'
#
#     col = col[::-1] #col값을 구했다!
#
#     #색칠해야하는 거 구하기
#     cnt = 0
#     for _ in range(N):
#         cnt += M -lst[_][col[_]]
#     print(f'#{tc} {cnt}')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    ans = 0
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            cnt = 0
            for s in range(0, i+1):
                cnt += arr[s].count('W')
            for s in range(i+1, j+1):
                cnt += arr[s].count('B')
            for s in range(j+1, N):
                cnt += arr[s].count('R')
            ans = max(ans, cnt)
    print(f'#{tc} {N*M - ans}')





