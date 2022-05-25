import re


def main(s):
    pattern = r'loc[\w:=\s\.]*'
    res = re.findall(pattern, s)
    ' '.join(res)
    pattern2 = r'\w[\w\ ]*'
    res = re.findall(pattern2, s)
    res = ' '.join(res)
    res = res.replace('do', '')
    res = res.replace('loc', '')
    res = res.replace('od', '')
    res = res.split(' ')
    res = list(filter(None, res))
    res = dict(zip(res[::2], res[1::2]))
    return res


print(main(
    'do { loc teat_733 := onzaqu_972.},{ loc ceed := enaran_325. }, {loc\norin_897 :=bisobi_211. },{ loc atusor:= been_581. }, od'))
