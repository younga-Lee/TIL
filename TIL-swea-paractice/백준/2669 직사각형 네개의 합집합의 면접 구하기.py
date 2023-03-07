arr = [list(map(int, input().split())) for _ in range(4)]
cnt_list = [[0]*101 for _ in range(101)]

for i in range(len(arr)):
    for j in range(arr[i][0], arr[i][2]): #꼭지점 좌표이므로 -1 해줘야함.
        for k in range(arr[i][1], arr[i][3]):
            cnt_list[j][k] = 1
cnt = 0
for a in range(len(cnt_list)):
    for b in range(len(cnt_list)):
        if cnt_list[a][b] == 1:
            cnt += 1
print(cnt)


#------------------잘 했는데 cnt출력에서 문제 생김,, 꼼수 하려고 하지말고 곧이 곧대로 해보자.