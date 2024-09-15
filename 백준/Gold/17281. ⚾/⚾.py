from itertools import permutations

# 입력 받기
N = int(input())  # 이닝 수
game = [list(map(int, input().split())) for _ in range(N)]  # 각 이닝의 결과

# 선수들의 순서 중 1번 선수(인덱스 0번)는 4번 타자로 고정
order = list(range(1, 9))  # 1번 선수를 제외한 선수들 (1~8번)

result = 0  # 최대 점수를 저장할 변수

# 1번 선수를 4번 타자로 고정한 순열을 생성
for x in permutations(order, 8):
    batter = list(x[:3]) + [0] + list(x[3:])  # 4번 타자는 1번 선수 (인덱스 0번)
    number, point = 0, 0  # 타순과 점수를 초기화

    # 각 이닝을 처리
    for i in range(N):
        out_count = 0  # 현재 이닝에서의 아웃 수
        p1, p2, p3 = 0, 0, 0  # 1루, 2루, 3루에 주자가 있는지 여부
        
        # 3아웃이 되기 전까지 타순에 따라 계속 타석에 들어감
        while out_count < 3:
            action = game[i][batter[number]]  # 현재 타자가 한 행동 (안타, 홈런 등)
            
            if action == 0:  # 아웃
                out_count += 1
            elif action == 1:  # 안타
                point += p3  # 3루 주자는 득점
                p1, p2, p3 = 1, p1, p2  # 모든 주자 한 베이스씩 이동
            elif action == 2:  # 2루타
                point += p2 + p3  # 2루와 3루 주자는 득점
                p1, p2, p3 = 0, 1, p1  # 주자는 두 베이스씩 이동
            elif action == 3:  # 3루타
                point += p1 + p2 + p3  # 모든 주자는 득점
                p1, p2, p3 = 0, 0, 1  # 타자는 3루까지 이동
            elif action == 4:  # 홈런
                point += p1 + p2 + p3 + 1  # 모든 주자 + 타자 득점
                p1, p2, p3 = 0, 0, 0  # 모든 주자 초기화

            # 다음 타자로 넘어감
            number = (number + 1) % 9  # 타순이 9가 되면 다시 0으로 초기화

    # 최대 점수를 갱신
    result = max(result, point)

# 최대 점수 출력
print(result)
