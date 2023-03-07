import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
num = deque(list(range(1, N+1)))
ans = []


while num:
    num.rotate(-K)
    ans.append(num.pop())

print('<', end = '')
print(*ans, sep=', ', end='')
print('>')
