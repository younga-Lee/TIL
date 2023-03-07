T = int(input())

for ts in range(1,T+1):
    score = list(map(int, input().split()))
    total = 0
    for i in score:
        if i < 40: total += 40
        else: total += i

    print(f'#{ts} {round(total/len(score))}')