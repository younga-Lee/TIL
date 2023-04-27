T = int(input())
for _ in range(T):
    number = input()
    N = len(number)
    stk = []
    lst = []
    for i in range(N):
        if number[i] == '>':
            while stk:
                lst.append(stk.pop())
        elif number[i] == '-':
            if lst:
                lst.pop()
        elif number[i] == '<':
            if lst:
                stk.append(lst.pop())
        else:
            lst.append(number[i])

    while stk:
        lst.append(stk.pop())
    print(''.join(lst))