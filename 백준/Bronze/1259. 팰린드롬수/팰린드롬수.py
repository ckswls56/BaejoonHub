

def check(a,b):
    if a==b:
        print("yes")
    else:
        print("no")

s = input()

while s != '0':
    
    l = len(s)
    
    
    if l % 2 == 0:
        check(s[:l//2],s[l//2:][::-1])
        
    else :
        check(s[:l//2],s[l//2+1:][::-1])
    
    s = input()