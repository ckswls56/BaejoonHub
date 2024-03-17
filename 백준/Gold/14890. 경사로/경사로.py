def all_elements_equal(lst):
    return len(set(lst)) == 1


def cross(arr):
    ramp = set()
    i = 1
    while i < len(arr):
        if arr[i-1] == arr[i]:
            i+=1
        elif arr[i-1]>arr[i] and arr[i-1]-1 == arr[i]:
            if (i+l) <= len(arr):
                if all_elements_equal(arr[i:i+l]):
                    for k in range(i,i+l):
                        if k not in ramp :
                            ramp.add(k)
                        else :
                            return False
                    else :
                        i+=l
                else :
                    return False
            else :
                return False
        elif arr[i-1]<arr[i] and arr[i-1] == arr[i]-1:
            if (i-l) >= 0:
                if all_elements_equal(arr[i-l:i]):
                    for k in range(i-l,i):
                        if k not in ramp :
                            ramp.add(k)
                        else :
                            return False
                    else :
                        i+=1
                else :
                    return False
            else :
                return False
        else :
            return False


    
    return True




n,l = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
answer = 0
for i in range(len(arr)):
    if cross(arr[i]):
        answer += 1
        
y_arr = list(zip(*arr))
for i in range(len(y_arr)):
    if cross(y_arr[i]):
        answer += 1
        
print(answer)