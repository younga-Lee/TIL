# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 반드시 재귀함수로 구현해야 합니다.
def dec_to_bin(number):
    
    answer = ''
    
    if number%2 == 1:
        answer += '1'
    else:
        answer += '0'
    
    if number > 1:
        answer = str(number%2) + str(dec_to_bin(number//2))
        number = number//2
        
    return answer[::-1]


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010
