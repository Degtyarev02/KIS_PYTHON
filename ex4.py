import cmath
import math


def main(n):
    if n == 0:
        return -0.08
    if n == 1:
        return 0.05
    if n >= 2:
        return (math.log(89 + main(n - 1) + 4 * (main(n - 2) ** 3)) ** 3) - 58


print(main(2))
