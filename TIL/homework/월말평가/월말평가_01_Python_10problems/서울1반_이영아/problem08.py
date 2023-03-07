# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    secret = []
    upper_acii = list(range(65,91))
    lower_acii = list(range(97,123))
    
    for s in word:
        if chr(ord(s) + n).islower() and (ord(s) + n) in lower_acii:
            secret.append(chr(ord(s) + n)) #소문자이자 정상 범위
        elif chr(ord(s) + n).isupper() and (ord(s) + n) in upper_acii:
            secret.append(chr(ord(s) + n)) #대문자이자 정상 범위
        else:
            secret.append(chr(ord(s) + n-26)) #정상 범위를 벗어날 경우
    return ''.join(secret)

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
