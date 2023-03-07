#11650 좌표 정렬하기
# 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성
import sys
input = sys.stdin.readline
n = int(input())

l = [tuple(map(int,input().split())) for _ in range(n)] # 좌표를 1차원 튜플로 만든 후, 리스트에 넣기
l_1 = sorted(l, key = lambda x: (x[0],x[1])) #x,y좌표 차례대로 정렬
 
for i in l_1:
    print(*i)
    
# --- 배운점 ---
#sorted에서 람다 함수 이용하면 x, y 차례대로 정렬가능임!
#시간 초과 ㅠ -> 입력을 sys으로 해야함