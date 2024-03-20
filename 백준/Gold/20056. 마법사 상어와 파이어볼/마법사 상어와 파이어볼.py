def is_all_odd_or_even(lst):
    first_element_parity = lst[0] % 2  # 첫 번째 원소의 홀짝 여부를 저장합니다.
    
    # 모든 원소를 순회하면서 첫 번째 원소와 홀짝 여부가 같은지 확인합니다.
    for element in lst[1:]:
        if element % 2 != first_element_parity:
            return False
    
    return True

n,m,k = map(int,input().split())
fireball = []
for i in range(m):
    r,c,m,s,d = map(int,input().split())
    fireball.append((r-1,c-1,m,s,d))

direction = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]


while k:
    k-=1
    new_fireball = {}

    for y,x,m,s,d in fireball:
        if m > 0:
            dy,dx = (y+direction[d][0]*s)%n,(x+direction[d][1]*s)%n

            if (dy,dx) in new_fireball:
                new_fireball[(dy,dx)].append((m,s,d))
            else :
                new_fireball[(dy,dx)]=[]
                new_fireball[(dy,dx)].append((m,s,d))

    fireball.clear()
    
    for key,v in new_fireball.items():
        y,x = key
        if len(v)>=2 :
            sum_m,sum_s,sum_d = tuple(sum(x) for x in zip(*v))
            
            if is_all_odd_or_even([x[2] for x in v]):
                dir = [0,2,4,6]
            else :
                dir = [1,3,5,7]
            for d in dir:
                fireball.append((y,x,sum_m//5,sum_s//len(v),d))
        else :
            m,s,d = v[0]
            fireball.append((y,x,m,s,d))

ans = 0
for fire in fireball:
    ans+=fire[2]

print(ans)