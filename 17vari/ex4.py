import math


def main(n):
    if n == 0:
        return 0.72
    if n == 1:
        return 0.55
    else:
        return (((main(n - 2) ** 3) + ((main(n - 1)) / 74)) ** 3) - main(n-1)


print(main(5))
print(main(9))
