
n,k = map(int,input().split())
a = list(input())

eat = [False] * n

ans = 0

for i in range(n):
    
    if a[i] == 'P':
        
        for j in range(i-k,i+k+1):
            if 0<=j<n:
                if not eat[j] and a[j] == 'H':
                    eat[j] = True            
                    ans += 1
                    
                    break

print(ans)