T = int(input())

for tc in range(1, T+1):
    N, P = map(int, input().split())

    a, b = divmod(N, P) #몫, 나머지


    print(f'#{tc}', a, b)