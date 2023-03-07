from collections import deque
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split()) #문서의 개수, 몇번 째로 인쇄되었는지 궁금한 문서가 몇번째 인지
    ip = list(map(int, sys.stdin.readline().rstrip().split())) #중요도
    arr = list(range(1, N+1))
    do = N[M]

    while ip:
        t = ip[0]
        if max(ip) != t: #가장 중요한 것이 아닐 때 인쇄하지 않음
            ip.rotate(-1)
        else:
            ip.leftpop()
            arr.leftpop()
    print(ip)
