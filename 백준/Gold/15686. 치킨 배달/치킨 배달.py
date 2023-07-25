from collections import deque
from itertools import combinations
import math

n, m = map(int, input().split())

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def bfs(chosen_chickens):
    total_distance = 0
    for house in houses:
        min_dist = float('inf')
        for chicken in chosen_chickens:
            dist = distance(house, chicken)
            min_dist = min(min_dist, dist)
        total_distance += min_dist
    return total_distance

arr = []
houses = []
chickens = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(n):
        if row[j] == 1:
            houses.append((i, j))
        elif row[j] == 2:
            chickens.append((i, j))

# m개의 치킨집 선택하는 경우의 수 계산
chicken_combinations = list(combinations(chickens, m))

min_distance = float('inf')

for chosen_chickens in chicken_combinations:
    total_dist = bfs(chosen_chickens)
    min_distance = min(min_distance, total_dist)

print(min_distance)
