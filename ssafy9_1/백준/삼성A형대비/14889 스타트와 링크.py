def check(place):
    dr1 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dr2 = [[(-1, 1), (1, 1)], [(-1, -1), (1, -1)], [(1, 1), (1, -1)], [(-1, 1), (-1, -1)]]
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                for dr in range(4):
                    ni, nj = i + dr1[dr][0], j + dr1[dr][1]

                    #맨하튼 거리가 1일 때
                    if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == "P":
                        return 0
                    #맨하튼 거리가 2일 때
                    if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == "O":
                        si, sj = ni + dr1[dr][0], nj + dr1[dr][1]
                        if 0<=si<5 and 0<=sj<5 and place[si][sj] == "P":
                            return 0

                        for di2, dj2 in dr2[dr]:
                            ei, ej = i + di2, j + dj2
                            if 0<=ei<5 and 0<=ej<5 and place[ei][ej] == "P":
                                return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer

solution([["POOPO", "OOOOO", "OOOXP", "OPOPX", "OOOOO"]])