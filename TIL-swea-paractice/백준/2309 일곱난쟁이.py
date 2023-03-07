kee = sorted([int(input()) for _ in range(9)])

difference = sum(kee) - 100

a = b = 0
for i in range(len(kee)):
    for j in range(i+1, len(kee)):
        if kee[i]+kee[j] == difference:
            for k in range(len(kee)):
                if k == i or k == j:
                    pass
                else:
                    print(kee[k])
            exit() #강제종료
