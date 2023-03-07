
def bfs(v, N):
	visited = [0]*(N+1) #visited생성
	q = [v] #큐생성
								#시작점 인큐
	visited[v] = 1 #시작점 인큐표시
	while q: #큐가 비어있지 않으면
		t = q.pop(0) #디큐
		print(t, end = ' ') #t에서 처리할 일
		for v in adjl[t] : #t에 인접이고 방문한 적 없는 v
			if visited[v] == 0:
					q.append(v)  #v 인큐
					visited[v] = visited[t] + 1 #v 인큐되었음 표시

V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjL = [[] for _ in range(V+1)] #인접리스트/ 누구랑 연결되어 있는지

for i in range(E):
	v1, v2 = arr[i*2], arr[i*2+1]
	adjL[v1].append(v2)
	adjL[v2].append(v1)