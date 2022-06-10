def main(x):
    if x[0] == 'NESC':
        return 10
    if x[4] == 1976:
        return {
            'GO': 0,
            'GOSU': 1
        }.get(x[2], 2)
    if x[1] == 1960:
        return 3
    if x[1] == 2013:
        return {
            'GO': 4,
            'GOSU': 5
        }.get(x[2], 6)
    return {
        2010: 7,
        1996: 8,
    }.get(x[3], 9)

print(main(['RAGEL', 1957, 'GOSU', 2010, 1996]))
print(main(['RAGEL', 2013, 'LOGOS', 1997, 1996]))
print(main(['NESC', 1960, 'GOSU', 1996, 1996]) )
