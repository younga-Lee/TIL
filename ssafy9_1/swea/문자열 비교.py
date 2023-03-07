T = int(input())

for ts in range(1, T+1) :
    str1 = input()
    str2 = input()
    if str1 in str2: ans = 1
    else: ans = 0
    print(f'#{ts} {ans}')
