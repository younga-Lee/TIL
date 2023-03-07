T = int(input())

for ts in range(1,T+1):
    word = input()
    if word == word[::-1] : ans = 1
    else: ans = 0

    print(f'#{ts} {ans}')