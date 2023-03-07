P = int(input())

for _ in range(P):
    lst = list(map(int, input().split()))
    t, lst = lst[0], lst[1:]
    cnt = 0

    for i in range(1, len(lst)):
        for j in range(i):
            if lst[j] > lst[i]:
                lst.insert(j, lst.pop(i))
                cnt += i #학생들이 뒤로 물러난 걸음 수 !!! (모든 학생들인 것을 간과함) -> 앞 사람만 이동, 뒤는 그대로

    print(t, cnt)