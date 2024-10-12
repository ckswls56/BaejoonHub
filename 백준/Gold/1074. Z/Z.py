N, r, c = map(int, input().split())

def z(n, y, x, cnt):
    if n == 1:
        if y == r and x == c:
            return cnt
        elif y == r and x + 1 == c:
            return cnt + 1
        elif y + 1 == r and x == c:
            return cnt + 2
        elif y + 1 == r and x + 1 == c:
            return cnt + 3
        return None

    size = 2**(n - 1)
    if r < y + size and c < x + size:
        return z(n - 1, y, x, cnt)  # 1st quadrant
    elif r < y + size and c >= x + size:
        return z(n - 1, y, x + size, cnt + size * size)  # 2nd quadrant
    elif r >= y + size and c < x + size:
        return z(n - 1, y + size, x, cnt + 2 * size * size)  # 3rd quadrant
    else:
        return z(n - 1, y + size, x + size, cnt + 3 * size * size)  # 4th quadrant

result = z(N, 0, 0, 0)
print(result)
