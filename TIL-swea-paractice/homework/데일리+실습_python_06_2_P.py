grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

#작물과 가격이 함께 있는 리스트가 존재할 때, 가장 높은 가격을 가지고 있는 작물의 이름을 출력하라.
# 단, 작물의 이름을 직접 입력하여 출력하지 않는다.

price = [grain_lst[i][1] for i in range(len(grain_lst))]
plant = [grain_lst[i][0] for i in range(len(grain_lst))]
max_index = price.index(max(price))
print(plant[max_index])