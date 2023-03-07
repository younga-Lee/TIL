#가장 큰 종이 조각의 넓이

r, c = map(int, input().split())
cut = int(input())
arr = [[0]*r for _ in range(c)] #직사각형 모양의 종이

for _ in range(cut):
    line = map(int, input().split())

print(arr)