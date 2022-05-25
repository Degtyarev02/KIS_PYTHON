def main(x):
    sum = 0
    for i in range(0, len(x)):
        sum += (x[i] ** 3 + 60 + 3 * x[i]) ** 6
    return 57 * sum


print(main([0.78, -0.28, -0.49, -0.15, 0.83]))
