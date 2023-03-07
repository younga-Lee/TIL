#1181 단어 정렬
n = int(input())

l = [input() for i in range(n)]
l_0 = list(set(l)) # 중복제거
l_1 = sorted(l_0) # 길이가 같으면 사전 순으로
l_2 = sorted(l_1, key = len) # 길이가 짧은 것부터
 
print(*l_2, sep='\n')