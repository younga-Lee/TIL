T = int(input()) #총 테스트 개수
stu, num = map(int, input().split()) #학생수, 학점을 알고 싶은 학생의 번호
grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

#학생이 받은 시험 및 과제 점수
for ts in range(1, T+1):
    score = list(map(int,input().split()))
    total = score[0]*0.35 + score[1]*0.45 + score[2]*0.2
    d = dict()
    for i in range(1,stu+1): #학생당 총 점수 할당
        d[i] = total
    score_sorted = sorted(d, key = lambda x:-x[1])

    print(score_sorted)