score = {
    'python': 80,
    'django': 89,
    'web': 83
}

score['algorithm'] = 90 #알고리즘 성적 추가
score['python'] = 85 #파이썬 성적 수정

print(sum(score.values())/len(score)) #전체 과목 평균 점수