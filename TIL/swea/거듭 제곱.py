def power(n, m):
    if m == 0:
        return 1 #끝낼 조건!! f(0)
    else:
        return power(n, m-1)*n #m이 하나씩 줄어들기

for _ in range(10):
    t = int(input())
    n, m = map(int, input().split()) #N의 M 거듭제곱 값

    print(f'#{t} {power(n, m)}')

