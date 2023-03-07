T = int(input())

for tc in range(1, T+1):
    lst = input()
    ans = [int(lst[i:i+7], 2) for i in range(0,len(lst), 7)]
    print(f'#{tc}', *ans)