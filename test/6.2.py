def main(x):
    return {
        1999: {
            2008: {
                1980: 0,
                1959: 1
            }.get(x[2], 2),
            1971: 3
        }.get(x[0], 4),
        1995: {
            1971: {
                1980: 6,
                1959: 7
            }.get(x[2], 8),
            1972: {
                'EJS': 9,
                'TEX': 10
            }.get(x[1], 11)
        }.get(x[0], 5)
    }.get(x[3], 12)


print(main([1971, 'EJS', 1980, 1995]))
print(main([2008, 'EJS', 1959, 1999]))
print(main([2008, 'C', 1984, 1999]))
