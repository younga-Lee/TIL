#1. 문자열을 전달 받아 해당 문자열의 모음 갯수를 반환하는 count_vowels 함수를 작성하시오.
def count_vowels(string):
    cnt = 0
    for s in string:
        if s in ['a','e','i','o','u']:
            cnt += 1
    return cnt


print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3
