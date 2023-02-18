import math


def main(x):
    if x < 93:
        return (1 + x ** 2 + (x ** 3 / 17)) ** 7 + x ** 2
    elif 93 <= x < 144:
        return 0.01 - x ** (5 / 2)
    elif 144 <= x < 193:
        return (12 * (31 - (x / 35) - 2 * x ** 3) ** 5)
    else:
        return 5 - 40 * math.cos(x) ** 6
