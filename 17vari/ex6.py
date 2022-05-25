def main(x):
    if x[2] == 'OX':
        return 10
    if x[4] == 1980:
        if x[0] == 'HTTP':
            if x[1] == 2008:
                return 7
            if x[1] == 1976:
                return 8
            return 9
        if x[0] == 'ASP':
            if x[1] == 2008:
                return 4
            if x[1] == 1976:
                return 5
            return 6
        if x[3] == 'CLICK':
            return 2
        return 3
    if x[3] == 'CLICK':
        return 0
    return 1


print(main(['HTTP', 1976, 'OX', 'CLICK', 1986]))
