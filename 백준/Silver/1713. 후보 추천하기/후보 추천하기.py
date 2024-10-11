
#사진 틀 개수
n = int(input())
#총 추천횟수
m = int(input())

recommend = list(map(int,input().split()))

photo = []

photo.append([1,0,recommend[0]])

for i in range(1,len(recommend)):
    flag = False
    for j in range(len(photo)):
        if recommend[i] == photo[j][2]:
            photo[j][0] += 1
            flag = True
            break
    
    if not flag:
        if len(photo) < n:
            photo.append([1,i,recommend[i]])
        else :
            photo.sort(reverse=True)
            photo.pop()
            photo.append([1,i,recommend[i]])
            

photo.sort(key = lambda x : x[2])

for _,_,student in photo:
    print(student,end=" ")