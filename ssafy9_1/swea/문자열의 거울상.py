T = int(input())
for ts in range(1, T+1):
    S = input()
    answer = ''

    for s in S[::-1]:
        if s == 'p' : answer += 'q'
        if s == 'q': answer += 'p'
        if s == 'b': answer += 'd'
        if s == 'd': answer += 'b'

    print(f'#{ts} {answer}')