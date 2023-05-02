import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N,M = map(int, input().split())
#집합생성
sets = []
for n in range(N+1):
    sets.append({n})

copy_sets = sets.copy()
a_set, b_set = [], []
for _ in range(M):
    ip, a, b = map(int, input().split())
    if ip == 0: #집합 합치기
        if a != b:
            for i in range(len(copy_sets)):
                if a in copy_sets[i]:
                    a_set = copy_sets[i]
                if b in copy_sets[i]:
                    b_set = copy_sets[i]
                if a_set !=[] and b_set !=[]:
                    break
            copy_sets.append(a_set | b_set)
            copy_sets.remove(a_set)
            copy_sets.remove(b_set)
            a_set, b_set = [], []
    if ip == 1: #두 원소가 같은 집합에 있는지 확인
        for i in range(len(copy_sets)):
            if a in copy_sets[i]:
                if b in copy_sets[i]:
                    print("YES")
                    copy_sets = sets.copy()
                    break
                else:
                    print("NO")
                    copy_sets = sets.copy()
                    break
