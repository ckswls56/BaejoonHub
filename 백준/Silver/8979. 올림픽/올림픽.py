n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 금메달, 은메달, 동메달 수를 기준으로 내림차순 정렬
arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))

# 초기값 설정

count = 0  # 동점자 수
rank = 0
prev_gold, prev_silver, prev_bronze = 0,0,0
# 첫 번째 국가 메달 수
# 국가 K의 메달 정보 저장
for i in range(n):
    if arr[i][0] == k:
        prev_gold, prev_silver, prev_bronze = arr[i][1], arr[i][2], arr[i][3]
        rank = i
        break


for i in range(rank-1, -1, -1):
    if prev_gold == arr[i][1] and prev_silver == arr[i][2] and prev_bronze == arr[i][3]:
        count+=1
    else :
        break
    
    

print(rank-count+1)
