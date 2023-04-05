'''
4 5
00110
00011
11111
00000
'''

def dfs(x, y):
  #주어진 범위 벗어나면 즉시 종료
  if x <= -1 or x >= N or y <=-1 or y >= M:
    return False
  #현재 노드를 아직 방문하지 않았다면
  if arr[x][y] == 0:
    arr[x][y] = 1 #방문처리
    #상하좌우 재귀적으로 호출
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    dfs(x+1,y)
    return True
  return False


N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]
result = 0
for i in range(N):
  for j in range(M):
    if dfs(i,j) == True:
      result += 1
print(result)