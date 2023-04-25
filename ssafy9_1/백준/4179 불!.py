from collections import deque
def bfs(ji,jj, fire):
    q = deque([(ji,jj)])
    while q:
        i, j = q.popleft()
        for di, dj in dr:
            ni,nj = di+i,dj+j
            if arr[ni][nj] == '@': #미로탈출
                return len(arr[i][j])

            #자리이동
            if 0<=ni<N+2 and 0<=nj<M+2 and arr[ni][nj] == '.':
                q.append((ni,nj))
                arr[ni][nj] += arr[i][j]

                #자리이동 후 불 퍼지기
                for fi, fj in fire:
                    for di, dj in dr:
                        ni2, nj2 = di + fi, dj + fj
                        if 0<=ni2<N+2 and 0<=nj2<M+2 and arr[ni2][nj2] != '#':
                            arr[ni2][nj2] = 'F'
    return "IMPOSSIBLE"

N, M = map(int, input().split())
arr = [['@']*(M+2)] + [['@']+list(list(input()))+['@'] for _ in range(N)] +[['@']*(M+2)]
dr = [(0,1),(0,-1),(1,0),(-1,0)]
fire = []
for a in range(1, N+1):
    for b in range(1, M+1):
        if arr[a][b] == 'J':
            ji, jj = a, b
        elif arr[a][b] == 'F':
            fire.append((a, b))
print(bfs(ji,jj, fire))

#불이 발생하는 곳 두군데 이상