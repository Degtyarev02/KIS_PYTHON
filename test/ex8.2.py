import re


def main(s):
    pattern = r'define[\w\ \'\=\:]*'
    res = re.findall(pattern, s)
    pattern = r'\'[\w\ \=\:]*'
    res = re.findall(pattern, s)
    res = filter(lambda val: val != "=:", res)
    res = ''.join(res)
    res = res.replace("=:", '')
    res = res.replace("'", '')
    res = res.split(" ")
    res = filter(lambda val: val != "", res)
    res = list(res)
    res = dict(zip(res[::2], res[1::2]))
    res = {y: x for x, y in res.items()}
    return res

print(main("{{{ define 'enonar' =: main_353 }}; {{define 'anined' =:tiesis_837}}; }"))