# 문제
# 1.    2개의 숫자를 인자로 받아 더하기 add, 빼기 sub, 곱하기 mul, 나누기 div연산의 결과를 반환하는 4개의 함수를 calc.py에 작성하시오.
# 단, 나누기 연산 중, ‘0’으로 나누려는 경우가 발생하면 try except 구문을 사용하여 문자열 “’0’으로는 나눌 수 없습니다.” 를 반환하시오..
# 앞서 작성한 calc.py 모듈을 import하여 각 연산을 수행하는 함수들을 실행하는 코드를 확인하시오.

import calc

print(calc.add(2, 3)) # 5
print(calc.sub(2, 3)) # -1
print(calc.mul(2, 3)) # 6
print(calc.div(2, 3)) # 0.6666666666666666

print(calc.div(2, 0)) # 0으로 나눌 수 없습니다.