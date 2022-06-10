import math


def main(y, z, x):
    n = len(x)
    result = 0
    for i in range(0, n):
        tmp = ((x[math.ceil(i // 4)] ** 3) / 56)
        result += (tmp + y[i] + (z[i] ** 2)) ** 5
    return result


print(main([0.47, -0.16, 0.2, 0.21, -0.63], [-0.89, -0.2, 0.58, -0.18, 0.68], [-0.91, 0.02, 0.93, -0.4, -0.04]))
