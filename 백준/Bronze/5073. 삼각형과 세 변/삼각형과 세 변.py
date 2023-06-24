a, b, c = map(int, input().split())
while(not(a == 0 and b == 0 and c == 0)):
    if(a+b <= c or a+c <= b or a+c <= b):
        print("Invalid")
    else:
        if(a == b and b == c and a == c):
            print("Equilateral")
        elif(a == b or b == c or a == c):
            print("Isosceles")
        else:
            print("Scalene")
    a, b, c = map(int, input().split())
