import sys

N = int(sys.stdin.readline().rstrip())

lst = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
lst1 = sorted(lst, reverse=True)
lst2 = sorted(lst, key= lambda x:x[1], reverse=True)

