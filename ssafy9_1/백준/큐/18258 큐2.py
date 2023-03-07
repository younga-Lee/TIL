from collections import deque
import sys
deq = deque()

N = int(input())
q = deque([])
for _ in range(N):
    a = sys.stdin.readline().rstrip()

    if 'push' in a:
        b = a.split()[1]
        q.append(int(b))
    if a == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    if a == 'size':
        print(len(q))
    if a == 'empty':
        if q:
            print(0)
        else:
            print(1)
    if a == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    if a == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
            
#deque가져오기, 빠르게 가져오기