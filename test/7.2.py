def main(x):
    f = (x & 0b1110_0000_0000_0000_0000_0000_0000_0000) >> 29
    e = (x & 0b0001_1111_1100_0000_0000_0000_0000_0000) >> 10
    d = (x & 0b0000_0000_0010_0000_0000_0000_0000_0000) >> 10
    c = (x & 0b0000_0000_0001_1111_1110_0000_0000_0000) >> 10
    b = (x & 0b0000_0000_0000_0000_0001_1111_1111_1110) << 18
    a = (x & 0b0000_0000_0000_0000_0000_0000_0000_0001) << 31
    return hex(a | b | c | d | e | f)

print(main(0x045ee71d))
print(main(0x042494f6))
print(main(0xf4488f79))
print(main(0xd0660799))
print(main(0x32460de8))