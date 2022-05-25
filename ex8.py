import re


def main(s):
    pattern = r'define[\w\s\\n:#-]*;'
    res = re.findall(pattern, s)
    bb = []
    for i in res:
        cc = []
        pat1 = r'\s[\w]*[\s:]?'
        res1 = re.search(pat1, i)
        strp = res1.group(0).split()
        strp = strp[0].split(':')
        cc.append(strp[0])
        pat2 = r'#[-\w]*;'
        res2 = re.search(pat2, i)
        stri = res2.group(0).split()
        cc.append(stri[0][1:-1])
        bb.append(cc)
    d = {}
    for i in range(len(bb)):
        d[bb[i][0]] = int(bb[i][1])
    return d

a = '[[ \\begin define isti : #8216; \\end. \\begin define lale_910 :#-3607;\n\\end. \\begin define quatied: #-8131; \\end.]]'
print(main(a))