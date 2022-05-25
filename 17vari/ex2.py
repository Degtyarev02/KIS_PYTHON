import math


def main(x):
    if x < -32:
        return 3 * math.exp(x) - (x ** 7 / 76)
    if -32 <= x < -5:
        return math.ceil(x**3-x**2-23*x)-x**6
    if x >= -5:
        return 54 * math.log2(x) ** 6 + (x**2/57) + 55*(x**4)

print(main(-15))
print(main(-62))