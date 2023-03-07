import sys
sys.stdin = open("s_input.txt", "r")

for tc in range(1, 11):
    N = int(input()) #항상 100
    arr = [list(map(int, input().split()))for _ in range(100)]

    for i in range(100):
