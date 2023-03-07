# def sum_of_digit(n):
#     return print(sum([int(i) for i in str(n)])) #반복문 사용


def sum_of_digit(n):
    n = str(n)
    print(n)
    if n == "":
        return 0
    return sum_of_digit(n[:-1]) + int(n[-1])

print(sum_of_digit(1234))

##우리가 해야하는 것: 힘수로 생각해보자.
# 1. 멈추는 조건 (if) :return하면 멈춤
# 2. args변화 : 재귀함수에서 달라지는 것은 input값 밖에 없음

# n =1234일때
#f(n) = f(n-1) + 4 (1234 = 123 + int(4))
#f(n-1) = f(n-2) + 3 (123 = 12 + int(3))
#f(n-2) = f(n-3) + 2 (12 = 1+int(2))
#f(n-3) = f(n-4) + 1 (1 = '' + int(1))