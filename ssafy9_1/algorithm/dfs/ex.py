from collections import deque
def solution(priorities, location):
    answer = 0
    N = len(priorities)

    priorities = deque(priorities)
    q.append(priorities.popleft())
    lst = [] #인쇄목록
    n = 0
    while priorities:
        J = q.pop()
        for i in range(len(priorities)):
            if priorities[0] < priorities[i]:
                priorities.append(J)
                q.append(priorities.popleft())
                n = (n+1)%N
                break
        else:
            q.append(priorities.popleft())
            n = (n+1)%N
            lst.append(n)
    return lst

lst = solution([1, 1, 9, 1, 1, 1], 0)
print(lst)
for j in range(len(lst)):
    if lst[j] == 0:
        print(j+1)
else:
    print(len(lst)+1)