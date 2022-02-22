import math


def main(y, z, x):
    result = ((7 * ((69 * y - 52 * (x ** 3) - 20 * (
            x ** 2)) ** 4) + ((math.log2(z ** 2) ** 5) / 39)) / (
                      47 * (y ** 2) + ((76 * z + (x ** 3)) ** 2))
              + (45 * (math.cos(76 * x + 94 * (
                    z ** 3)) ** 3)) - 17 * (math.sqrt(y) ** 7))
    return result


print(main(0.71, 0.38, 0.78))
