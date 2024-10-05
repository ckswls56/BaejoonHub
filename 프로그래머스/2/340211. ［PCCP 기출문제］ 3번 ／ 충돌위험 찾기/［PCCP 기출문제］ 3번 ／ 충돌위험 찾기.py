
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
from collections import defaultdict


def solution(points, routes):
    # 포인트 번호에 따른 좌표 정보 저장
    point_dict = {i + 1: (points[i][0], points[i][1]) for i in range(len(points))}

    # 시간별 좌표마다 로봇이 도착한 횟수를 저장하는 딕셔너리
    time_position_count = defaultdict(int)

    # 로봇들의 이동 경로 처리
    for route in routes:
        current_time = 0

        # 0초일 때 첫 포인트에 도착하는 것을 기록
        start_point = point_dict[route[0]]
        time_position_count[(current_time, start_point[0], start_point[1])] += 1

        for i in range(len(route) - 1):
            start = point_dict[route[i]]
            end = point_dict[route[i + 1]]

            # 현재 위치에서 목표 위치로 이동 (r 좌표를 먼저 이동, 그 다음 c 좌표 이동)
            r_start, c_start = start
            r_end, c_end = end

            # r 좌표 이동
            while r_start != r_end:
                if r_start < r_end:
                    r_start += 1
                else:
                    r_start -= 1
                current_time += 1
                time_position_count[(current_time, r_start, c_start)] += 1

            # c 좌표 이동
            while c_start != c_end:
                if c_start < c_end:
                    c_start += 1
                else:
                    c_start -= 1
                current_time += 1
                time_position_count[(current_time, r_start, c_start)] += 1

    # 충돌 횟수 계산
    danger_count = 0
    for value in time_position_count.values():
        if value > 1:
            danger_count += 1  # 충돌은 도착한 로봇 수 - 1 번 발생

    return danger_count