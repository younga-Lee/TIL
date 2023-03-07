from collections import Counter
N, K = map(int, input().split()) #전체 학생 수, 한방 최대 인원 수

stu = [tuple(map(int, input().split())) for n in range(N)]
cnt_stu = dict(Counter(stu))

room = 0
for v in cnt_stu.values():
    room += 1
    if v > K :
        room += v//K
print(room)