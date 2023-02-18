def main(a, n, z):
    temp = 1
    res = 0
    for i in range(1, n + 1):
        for k in range(1, a + 1):
            temp *= 22 * (z ** 2 + 88 * k ** 3 + (k / 99)) ** 4 - abs(i) ** 3
        res += temp
        temp = 1
    return res
