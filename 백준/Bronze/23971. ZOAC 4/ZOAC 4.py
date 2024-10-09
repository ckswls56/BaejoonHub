h, w, n, m = map(int, input().split())

# Calculate the number of steps needed in both dimensions
rows = (h + n) // (n + 1)
cols = (w + m) // (m + 1)

# The answer is the product of rows and columns
ans = rows * cols

print(ans)
