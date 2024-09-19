from itertools import combinations

word = input()

arr = list(range(1,len(word)))
ans = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'

for f,s in list(combinations(arr,2)):
    
    first = list(word[:f])
    first.reverse()
    second = list(word[f:s])
    second.reverse()
    third = list(word[s:])
    third.reverse()
    ans = min(ans,"".join(first+second+third))


print(ans)