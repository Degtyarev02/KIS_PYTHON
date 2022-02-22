import math


def main(z):
    result = 0
    if z < 74:
        result += math.floor(z) ** 3
    if 74 <= z < 90:
        result += ((z - (z ** 3)) / 27) - (24 * ((21 * z) ** 3))
    if 90 <= z < 175:
        result += ((z ** 3) + 90 + 98 * z) ** 7
    if z >= 175:
        result += (69 * ((6 * z + 1) ** 4) + 0.01 + z ** 6)
    return result
print(main(171))

