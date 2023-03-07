N = int(input())

for n in range(1,N+1):
    n = str(n)
    #숫자에 369가 들어있으면 -로 바꾸기
    for i in ['3','6','9']:
        n = n.replace(i, '-')

    #숫자가 섞인 경우에는 -만 출력
    if (n.count('-') >= 1) and (n.count('-') != len(n)):
        n = (n.count('-'))*'-'
    # ----------------------------
    print(n, end = ' ')

#--- 숫자가 섞인 경우 찾으랴 좀 오래걸림 ㅠㅠ 범위 +1 안해서 틀림