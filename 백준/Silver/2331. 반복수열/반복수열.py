
def cal(a,p):
    a = str(a)
    
    ret = 0
    
    for i in a:
        ret += int(i)**p
        
    return ret


a,p = map(int,input().split())
count = {}
count[a] = 1
for _ in range(100):
    a = cal(a,p)
    count[a] = count.get(a,0) + 1


ans = 0

for c in count.values():
    if c == 1:
        ans += 1
        
print(ans)