T = int(input())

for tc in range(1, T+1):
    memory = input()
    N = len(memory)
    init = ['0']*N
    cnt = 0

    while ''.join(init) != memory:
        for i in range(N):
            if memory[i] != init[i]: #비교 했을 때 다르면
                cnt += 1
                for j in range(i, N): #한줄로 쭉 밀기
                    init[j] = memory[i]

    print(f'#{tc} {cnt}')