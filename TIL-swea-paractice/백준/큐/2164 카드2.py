from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())
num = deque(list(range(1, n+1)))

while len(num) != 1:
    num.popleft() #가장 위에 있는 카드
    num.append(num.popleft())

print(num[0])