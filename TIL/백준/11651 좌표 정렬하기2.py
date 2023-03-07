import sys
input = sys.stdin.readline

N = int(input())

l = [list(map(int, input().split())) for n in range(N) ]
l_2 = sorted(l, key = lambda x:(x[1],x[0]))
for i in l_2:
    print(*i)