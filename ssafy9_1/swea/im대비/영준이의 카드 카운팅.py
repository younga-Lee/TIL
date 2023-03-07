T = int(input())

for tc in range(1, T+1):
    dic = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    info = input()
    arr = [info[i:i+3] for i in range(0, len(info), 3)]
    ans = 0

    if len(set(arr)) != len(arr):
        print(f'#{tc} ERROR')
    else:
        for j in range(len(arr)):
            dic[arr[j][0]] -= 1
        print(f'#{tc}', *dic.values())