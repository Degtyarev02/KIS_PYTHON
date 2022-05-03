from struct import unpack


def main(file):
    a_adr = 0
    for byte in file:
        a_adr += 1
        if byte == 0x41:
            break

    a = {f'A{i}': None for i in range(1, 4)}
    b = {f'B{i}': None for i in range(1, 7)}
    c = {f'C{i}': None for i in range(1, 7)}
    d = {f'D{i}': None for i in range(1, 5)}
    temp = unpack('>HLb4LQbL8hbBHLdL', file[a_adr:a_adr + 72])
    b['B1'], b['B2'], b['B3'], *c_struct, \
        b['B5'], uint32_size, uint32_adr, a['A2'], a['A3'] = temp
    d_adrs = c_struct[0:4]
    c['C2'], c['C3'], c['C4'], *c5, c['C6'] = c_struct[4:]
    c['C5'] = [e for e in c5]

    temp = unpack(f'>{uint32_size}L',
                  file[uint32_adr:uint32_adr + uint32_size * 4])
    b['B6'] = list(temp)

    c['C1'] = []
    for d_adr in d_adrs:
        temp = unpack('>hLLHb', file[d_adr:d_adr + 13])
        d['D1'], f_arr_size, f_arr_adr, d['D3'], d['D4'] = temp
        temp = unpack(f'>{f_arr_size}f',
                      file[f_arr_adr:f_arr_adr + f_arr_size * 4])
        d['D2'] = list(temp)
        c['C1'].append(d.copy())

    a['A1'] = b
    b['B4'] = c
    return a


bytes = (b'PJQAv\xa7\x90\xfb\xd6\xbd\r\x00\x00\x00T\x00\x00\x00m\x00\x00\x00\x82\x00'
         b'\x00\x00\x9b{hy\xf9\xbb\x06|\x06P\xba\n\xe6\xac\xa7\xcf\x9d\xce\xf7j\x9ek'
         b' \xc8W\xe4\xe0^\x04l\xb0%\x00\x02\x00\x00\x00\xa8\xbf\xe9\x08\x928]c\x16'
         b'W\xf0"\x1b>\xe4\xa8\xe3\xbe\xd1S\x96\xd1\x03\x00\x00\x00\x02\x00\x00'
         b'\x00L\x888\xf4\xbfk\xb52\xbd\xb5\x87\xd3\xbd\xbd\x1bA\x15\xfb\x00'
         b'\x00\x00\x03\x00\x00\x00a\x17\x7fq?B\x81\x93?l\xc7Ii\x91\x00\x00\x00\x02'
         b'\x00\x00\x00z5\xd7\xee?\x0fp4>\x06SI>\xc5\xdc\x9a\x89\x10\x00\x00\x00'
         b'\x03\x00\x00\x00\x8f\xae\xd4L\xb2\xee\x99:\x9ci%\xc0')
print(main(bytes))
bytes = (b'PJQA\x85\x06\xfe\xbe\xa4M\xde\x00\x00\x00X\x00\x00\x00q\x00\x00\x00\x86\x00'
         b'\x00\x00\xa33\xedOL\xeb^\xbf\xd7\x00\xf8\x0b\r\xca\xf2;\x0c\xd6\x819\xcf\x00'
         b'TSff\xa6\xecs!\x89\xd8\x00\x02\x00\x00\x00\xb0?\xaf9\x17{\xd3v\x80=o\xb2\xe6'
         b'>\xce\x10;\xbff\xe2n?K\xa1-k\xab\x00\x00\x00\x03\x00\x00\x00L\xe7a'
         b'\xc8\xbfI\xd3v\xbf`~\x9b>\x18$\xf1g\r\x00\x00\x00\x03\x00\x00\x00e5'
         b'f\x01\xbd\xc9\x97\x1f\xbf.s\x8b\x07b\x00\x00\x00\x02\x00\x00\x00~'
         b'\xfc\x08\xa2\xbe\xbb\xc5\xf2\xbf7\xde\xd7?\x05\xae\x17\xbe\xaa\x80\n\xa9'
         b'\\\x00\x00\x00\x04\x00\x00\x00\x93\xc9\n\xc1\n\xa4\xa6?tI\xfd\xa1')
print(main(bytes))
