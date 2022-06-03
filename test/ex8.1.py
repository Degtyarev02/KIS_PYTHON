import re


def main(s):
    pattern = r'auto[\w\s\=>@\'.]*'
    res = re.findall(pattern, s)
    pattern = r' [\w\s\=>@.\']*'
    res = re.findall(pattern, s)
    res = ''.join(res)
    res = res.split(" ")
    res = filter(lambda val: val != "auto", res)
    res = filter(lambda val: val != "==>", res)
    res = filter(lambda val: val != "", res)
    res = list(res)
    res = ''.join(res)
    res = res.split("@")
    res = ''.join(res)
    res = res.split("'")
    res = filter(lambda val: val != "", res)
    res = list(res)
    res = dict(zip(res[::2], res[1::2]))
    res = {y: x for x, y in res.items()}
    return res

print(main("do || auto beorus ==> @'diso'; || || auto bele ==> @'enen'; || || auto edareer_333 ==> @'esxeus_848'; || || auto enre ==> @'riinar_261'; ||done"))
