import math


def main(x):
    a = math.sqrt(85 * (24 * x - 1))
    b = ((x ** 3 - 62 - (x * x / 84)) ** 4 / (87)) - (x * x / 57)
    c = 54 * ((x ** 3 / 36) - 0.01) ** 6 + (x ** 3 + 1 + x ** 2) ** 2
    return a + (b / c)


print(main(0.98))
