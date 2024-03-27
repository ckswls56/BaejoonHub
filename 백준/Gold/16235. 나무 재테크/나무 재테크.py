from collections import deque

N, M, K = map(int, input().split())

land = [[5] * N for _ in range(N)]

A = [list(map(int, input().split())) for _ in range(N)]

tree_info = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, age = map(int, input().split())
    tree_info[r - 1][c - 1].append(age)

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for year in range(K):
    for r in range(N):
        for c in range(N):
            new_tree = deque()
            next_land = 0
            for age in tree_info[r][c]:
                if land[r][c] >= age:
                    land[r][c] -= age
                    new_tree.append(age + 1)
                else:
                    next_land += age // 2
            land[r][c] += next_land
            tree_info[r][c] = new_tree

    tmp_trees = []
    for r in range(N):
        for c in range(N):
            for age in tree_info[r][c]:
                if age % 5 == 0:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N:
                            tmp_trees.append((nr, nc))
            land[r][c] += A[r][c]

    for tree in tmp_trees:
        r, c = tree
        tree_info[r][c].appendleft(1)

total_trees = sum(len(tree) for row in tree_info for tree in row)
print(total_trees)