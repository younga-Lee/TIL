# import sys
# sys.stdin = open("s_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    memory = list(input())
    init = ['0'] * len(memory)
    cnt = 0

    for i in range(len(memory)):
        while init[i] != memory[i] and i < len(memory):
            if memory[i] == '1':
                for j in range(i, len(memory)):
                    init[j] = '1'
            else:
                for j in range(i, len(memory)):
                    init[j] = '0'
            cnt += 1


    print(f'#{tc} {cnt}')