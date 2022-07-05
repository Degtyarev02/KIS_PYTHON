import math

def main(n):
    if n == 0:
        return -0.92
    if n >= 1:
        return math.cos(main(n - 1) + (main(n - 1)) ** 3 + 1)

print(main(4))
print(main(3))
print(main(6))