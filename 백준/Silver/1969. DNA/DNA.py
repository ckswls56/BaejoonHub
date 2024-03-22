from collections import Counter
n,m = map(int,input().split())
dna = [input() for _ in range(n)]
hamming_distance = 0
hamming_code = ''
for d in zip(*dna):
    c = list(Counter(d).items())
    c.sort(key=lambda x : (-x[1],x[0]))
    c = c[0]
    
    hamming_distance += n-c[1]
    hamming_code += c[0]

print(hamming_code)
print(hamming_distance)