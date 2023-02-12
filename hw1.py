import math


def main(z, y, x):
    first_part = math.sqrt((6 * x ** 2 + 35 * z ** 3 + 31 * y) ** 4)
    second_part = ((abs(1 - 69 * x ** 3 - 55 * z ** 2) ** 7) / 25)
    fourth_part = 38 * (1 + y ** 3) ** 2
    third_part = 35 * (z ** 2 + x) ** 3 + (y ** 6 / 27)
    return first_part + (second_part - fourth_part) / third_part
