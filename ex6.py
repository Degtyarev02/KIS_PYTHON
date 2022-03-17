def main(x):
    if x[2] == 1982:
        if x[0] == 'CMAKE':
            if x[1] == 'CIRRU':
                match x[4]:
                    case 'ECL':
                        return 0
                    case 'GOSU':
                        return 1
                return 2
            if x[3] == 1982:
                return 3
            return 4
        if x[0] == 'LESS':
            if x[1] == 'CIRRU':
                if x[3] == 1982:
                    return 6
                return 7
            if x[3] == 1982:
                return 8
            return 9
        return 5
    return 10


print(main(['LESS', 'CIRRU', 1982, 1980, 'GOSU']))
print(main(['CMAKE', 'CIRRU', 1993, 1982, 'ECL']))
