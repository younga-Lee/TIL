# 문제
#  1.  어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.       
# 예를 들어 d(91) = 9 + 1 + 91 = 101일 때, n을 d(n)의 제네레이터(generator)라고 한다. 함수 fn_d(n)을 정의하여 보라
#  2.  어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.      
# 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.     
# 예를 들어 1, 3, 5, 7, 9, 20, 31 은 셀프 넘버들이다.
# 셀프넘버를 판별하는 함수 is_selfnumber(n)를 앞서 작성한 fn_d(n) 을 사용하여 작성하라.



# fn_d(91) 
# 출력 예시 
# 101

def fn_d(n):
    total = 0
    for i in range(len(str(n))):  #각 자릿수 숫자 더하기
        total += int(str(n)[i])
    return (total + n)

print(fn_d(91))  #조건1

def is_selfnumber(n):
    pass 