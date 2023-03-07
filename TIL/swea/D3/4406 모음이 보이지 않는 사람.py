T = int(input())

for ts in range(1, T+1):
    S = input()
    for s in ['a','e','i','o','u']:
        S = S.replace(s,'')
    print(f'#{ts} {S}')