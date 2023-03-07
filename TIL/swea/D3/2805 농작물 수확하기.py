import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for ts in range(1, T+1):
    N = int(input()) #농작물 크기
    for _ in range(N):
        word = input()
        for w in word:
            pass