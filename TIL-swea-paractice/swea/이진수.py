T = int(input())

for tc in range(1, T+1):
    a, b = input().split()
    val = format(int(b, 16), 'b').zfill(int(a)*4) #16진수 -> 2진수, 자릿수만큼 0 채우기
    print(f'#{tc} {val}')