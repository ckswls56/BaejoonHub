
n = int(input())
a = list(input())

# 빨간 파란색 min max index를 기준으로 
# 빨간색을 전부 왼쪽 or 오른쪽 , 파란색을 전부 왼쪽, 오른쪽 으로 옮기는것 중에 최소가 정답
min_r,max_r,min_b,max_b = n,0,n,0
for i in range(n):
    if a[i] == 'R':
        min_r = min(min_r,i)
        max_r = max(max_r,i)
    else:
        min_b = min(min_b,i)
        max_b = max(max_b,i)
if (min_r == n and max_r == 0) or (min_b == n and max_r == 0):
    print(0)
else:
    
    r_left,r_right,b_left,b_right =0,0,0,0
    for i in range(n):
        
        if a[i] == 'R':
            if min_b<i:
                r_left += 1
                
            if max_b>i:
                r_right += 1
        else :
            if min_r<i:
                b_left += 1
                
            if max_r>i:
                b_right += 1
            
    
    print(min(r_left,r_right,b_left,b_right))