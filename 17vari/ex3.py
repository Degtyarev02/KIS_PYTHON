import math


def main(m, y, b, x):
    iter1 = 0
    for i in range(1, m+1):
        iter1 += (82 * ((i ** 2 - 1) ** 5)) + (63 * (y ** 2))

    iter2 = 0

    for c in range(1, b+1):
        iter2 += 30 * (math.asin(x) ** 6) + (math.log2(x) ** 2) + 86 + c

    return iter1 + iter2


print(main(2, 0.19, 2, 0.32))
