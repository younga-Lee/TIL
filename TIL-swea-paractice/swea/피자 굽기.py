import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) #화덕의 크기, 피자개수
    pizza = list(map(int, input().split())) #피자들
    q = [] #화덕
    for i in range(1, N+1):
        q.append((i, pizza.pop(0)))


    while q:
        n, piz = q.pop(0) # 피자번호, 치즈량
        piz = piz // 2  # 치즈량 반으로 감소
        if piz == 0: #치즈가 다 녹으면
            if pizza: #남은 피자가 있다면
                i += 1
                q.append((i, pizza.pop(0)))  # 대기하고 있는 미조리 피자 순서대로 넣음
        else:
            q.append((n, piz))  # 다시 큐에 넣음

    print(f'#{tc}', n)
