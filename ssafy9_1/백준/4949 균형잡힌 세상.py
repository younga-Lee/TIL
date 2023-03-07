import sys
sys.stdin = open("ex.txt", "r")

ans = 'yes'
stack = []
d = {'(': ')', '[': ']'}

while True:
    con = input()
    if con == '.':
        break
    else:
        for i in con:
            if i in d:
                stack.append(d[i])
            elif i in d.values():
                if len(stack) != 0: #빈 리스트가 아닐 때 = 스택이 남아 있을 때
                    # if i != stack.pop():
                    #     ans = 'no'
                        break
                else:
                    ans = 'no'
                    break
    print(ans)
