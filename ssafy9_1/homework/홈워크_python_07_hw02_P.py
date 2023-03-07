# 문제
# 1937년 Collatz란 사람에 의해 제기된 이 추측은,
# 주어진 수가 1이 될때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측이다.
# 그 원리는 아래와 같다.

# 원리  i.입력된 수가 짝수라면 2로 나눈다. 
# ii. 입력된 수가 홀수라면 3을 곱하고 1을 더한다. 
# iii.결과로 나온 수에 같은 작업을 1이 될 때까지 반복한다.
# 예를 들어, 입력된 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 된다.
# 위 작업을 몇 번이나 반복해야하는지 반환하는 함수 collatz()를 작성하시오
# (단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환하시오.)

class Collatz:
    cnt = 0
    def __init__(self,n):
        self.n = n
        
    def even(self,n):
        if n%2 == 0:
            return n/2
        
    def odd(self, n):
        if n%2 == 1:
            return n*3 +1
    
    def collatz(self,n):
        self.cnt += 1
        self.even(n)
        self.odd(n)
        if self.cnt >= 500:
            return -1
        else:
            return self.cnt
# def collatz(n):
#     cnt = 0
#     while n != 1:
#         if n%2 == 0:
#             n = n/2
#         else:
#             n = n*3 +1
#         cnt += 1
        
#     if cnt >= 500:
#         return -1
#     else:
#         return cnt
    
collatz = Collatz()

collatz(6)  # => 8
collatz(16)  # => 4
collatz(27)  # => 111
collatz(626331)  # => -1
