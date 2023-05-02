from itertools import permutations

w, g = map(int, input().split())
word = list(input())
s = input()
cnt = 0

for i in permutations(word, w):
    if ''.join(i) in s:
        cnt += 1

print(cnt)