DAY = ['MON','TUE','WED','THU','FRI','SAT','SUN']

x,y = map(int,input().split())

MONTH = [0,31,28,31,30,31,30,31,31,30,31,30,31]

total = sum(MONTH[:x]) + y - 1

print(DAY[total%7])