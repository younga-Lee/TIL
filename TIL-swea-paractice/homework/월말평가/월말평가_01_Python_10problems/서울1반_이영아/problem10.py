# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    
    # N은 크기, M은 방향, position은 현위치
    position = list(position) # 튜플에서 변동가능한 리스트로 바꾸기
    
    #방향에 따라 위치 이동하기
    if M == 0 : 
        position[1] += 1
    elif M == 1 :
        position[1] -= 1
    elif M == 2 :
        position[0] -= 1
    elif M == 3 :
        position[0] += 1
    
    #범위확인
    if (0<= position[0] <= N) and (-N <= position[1] <= 0):
        return True
    else:
        return False
    
    
    
    


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
