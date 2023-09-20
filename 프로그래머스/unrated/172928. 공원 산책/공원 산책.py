def solution(park, routes):
    answer = []
    p = None  # 초기 S의 위치를 저장할 변수
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                p = i, j
                break  # 초기 S의 위치를 찾았으면 반복 중단
        if p is not None:
            break  # 초기 S의 위치를 찾았으면 반복 중단

    for r in routes:
        string = r.split(' ')
        direction = string[0]
        weight = int(string[1])
        flag = False

        if direction == 'N':
            if p[0] - weight >= 0:
                for i in range(p[0], p[0] - weight, -1):
                    if park[i][p[1]] == 'X':
                        flag = True
                        break
                if flag or park[p[0] - weight][p[1]] == 'X':
                    continue
                else:
                    p = p[0] - weight, p[1]

        elif direction == 'S':
            if p[0] + weight < len(park):
                for i in range(p[0], p[0] + weight):
                    if park[i][p[1]] == 'X':
                        flag = True
                        break
                if flag or park[p[0] + weight][p[1]] == 'X':
                    continue
                else:
                    p = p[0] + weight, p[1]

        elif direction == 'W':
            if p[1] - weight >= 0:
                for i in range(p[1], p[1] - weight, -1):
                    if park[p[0]][i] == 'X':
                        flag = True
                        break
                if flag or park[p[0]][p[1] - weight] == 'X':
                    continue
                else:
                    p = p[0], p[1] - weight

        else:
            if p[1] + weight < len(park[0]):
                for i in range(p[1], p[1] + weight):
                    if park[p[0]][i] == 'X':
                        flag = True
                        break
                if flag or park[p[0]][p[1] + weight] == 'X':
                    continue
                else:
                    p = p[0], p[1] + weight

    answer = p
    return answer
