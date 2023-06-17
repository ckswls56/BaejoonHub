matrix = []  # 2차원 리스트

for _ in range(9):  # 9줄에 대해 반복
    # 입력받은 값을 공백을 기준으로 분리하여 정수로 변환하여 리스트에 저장
    row = list(map(int, input().split()))
    matrix.append(row)  # 행을 2차원 리스트에 추가

max = 0
max_x=1
max_y=1
for i in range(9):
    for j in range(9):
        if(max<matrix[i][j]):
            max=matrix[i][j]
            max_x=j
            max_y=i

print(max)
print(max_y+1,max_x+1)
