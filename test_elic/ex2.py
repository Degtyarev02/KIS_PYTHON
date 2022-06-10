def main(x):
    if x[0] == 1991:
        return 10
    if x[2] == 'ATS':
        return 9
    if x[1] == 'GLYPH':
        return {
            'OPAL': 0,
            'LFE': 1
        }.get(x[3], 2)
    if x[1] == 'RAGEL':
        return {
            'OPAL': 3,
            'LFE': 4
        }.get(x[3], 5)
    if x[4] == 'IOKE':
        return 6
    if x[4] == 'SVG':
        return 7
    return 8


print(main([1960, 'GN', 'LOGOS', 'NSIS', 'IOKE']))
