def fast_mul(a, b):
    k = 1
    res = 0
    if (a < 0 and b > 0) or (a > 0 and b < 0): k = -1
    a = abs(a)
    b = abs(b)
    b1 = [b]
    if a % 2 != 0: res += b
    while a > 1:
        if (a // 2) % 2 != 0:
            b1.append(b * 2)
            res += b * 2
        a = a // 2
        b = b * 2
    return res * k


def fast_pow(a, x):
    k = 1
    res = 1
    if x < 0:
        k = -1
        x = abs(x)
    while x > 0:
        res *= a  # res = fast_mul(res, a)
        x -= 1
    if k == -1: return res ** (-1)
    return res


def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y

def mul16(x, y):
    x_top = x >> 8
    x_low = x & 0xff
    y_top = y >> 8
    y_low = y & 0xff
    #((xh * yh) * 2^8 + ((xh * yl) + (xl * yh)) * 2^4 + (xl * yl)
    return mul_bits(x_top, y_top, 16) * 2**8 + (mul_bits(x_top, y_low, 16) + mul_bits(x_low, y_top, 16)) * 2**4 + mul_bits(x_low, y_low, 16)

print(mul16(10, 5))
print(mul16(2,6))
