# def func(n):
#     if n == 0:
#         return
#     print(n)
#     func(n-1)
# func(10)


def fibo(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fibo(n-1) + fibo(n-2)

print(fibo(5)) 

#함수로 나타낸 후, 기본값을 멈추는 조건으로 둔다!!