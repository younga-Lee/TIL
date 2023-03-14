from collections import deque

n = int(input())
deq = deque()

def dq(o):
    if o[0] == 'push_front':
        deq.appendleft(int(o[1]))
        return None

    if o[0] == 'push_back':
        deq.append(int(o[1]))
        return None

    if o[0] == 'pop_front':
        if deq:
            return deq.popleft()
        else:
            print(-1)
    if o[0] == 'pop_back':
        if deq:
            return deq.pop()
        else:
           return -1
    if o[0] == 'size':
        return len(deq)

    if o[0] == 'empty':
        if deq:
            return 0
        else:
            return 1

    if o[0] == 'front':
        if deq:
            return deq[0]
        else:
            return -1

    if o[0] == 'back':
        if deq:
            return deq[-1]
        else:
            return -1

for _ in range(n):
    o = input().split()

    if dq(o) is not None:
        print(dq(o))

