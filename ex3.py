import math


def main(m, n, a):
    result = 0
    for i in range(1, a + 1):
        for j in range(1, n + 1):
            for k in range(1, m + 1):
                result += (2 * math.log(i)) - (
                        ((0.02 - (k ** 2) - j) ** 7) / 27) - 24 * (
                        (21 * j) ** 4)
    return result


print(main(7, 7, 8))
