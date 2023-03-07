    
def emoji_decorator(func):
    def wrapper(name):
        func(name)
        print('^~^//')
    return wrapper #wrapper이라는 함수를 리턴

    
def add_sad(func):
    def wrapper(name):
        func(name)
        print('ㅜ~ㅜ//')
    return wrapper

@add_sad #중복도 가능, 데코레이터 사용전에 함수 먼저 정의할 것.
@emoji_decorator
def ko_hello(name):
    print(f'안녕하세요, {name}님!')
    
@emoji_decorator
def en_hello(name):
    print(f'Hello, {name}!')
    


# def add_emoji(name, func): -> 불편
#     func(name)
#     print('^~^//')

    
# emoji_decorator(ko_hello)("Lee") #ko_hello가 실행되는 로직
# emoji_decorator(en_hello)("Lee")
#-> 더 간단하게 하려면 데코레이터 만들기
 
ko_hello("Lee")