import math


def main(y, z, x):
    tmp1 = 40 * ((53 * (z ** 3) - 35 - x ** 2) ** 2)
    tmp2 = (math.log2(z / 92 + 53 * x * x + y ** 3) ** 3) / 20
    tmp3 = ((y ** 2 + 17 + x ** 3) ** 6 - z ** 5) / (
                (abs(x ** 2 + (z / 23))) ** 5 + 53 * (63 * y ** 2 + 69 * z ** 3 + x) ** 4)
    return tmp1 - tmp2 + tmp3


print(main(-0.09, 0.86, -0.18))
