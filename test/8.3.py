import re

def main(x):
    pattern = r'\`[\w\s\:\#\(\)]*'
    x = re.findall(pattern, x)
    x = ''.join(x)
    x = x.split('`')
    x = ''.join(x)
    pattern = r'\ [\w\s]*'
    tmp1 = re.findall(pattern, x)
    tmp1 = list(filter(lambda val: val != ' ', tmp1))
    for i in range(len(tmp1)):
        tmp1[i] = tmp1[i].split(' ')
        tmp1[i] = list(filter(lambda val: val != '', tmp1[i]))
    x = x.split(" ")
    word1 = x[0]
    x = ''.join(x)
    pattern = r'\)[\w\:]*'
    x = re.findall(pattern, x)
    x = ''.join(x)
    x = x.split(")")
    x[len(x)-1] = word1
    x = list(filter(lambda val: val != '', x))
    tmp_word = x[0]
    x[0] = x[len(x)-1]
    x[len(x)-1] = tmp_word
    result = {}
    for j in range(len(x)):
        result[x[j]] = tmp1[j]
    print(result)

main("<: do val `tier : #( geen diri). done do val `ara_84 : #( cebeor_222 esatxe veso_437 ). done do val `isma_40: #(inbige bitior ). done do val `mare_753 : #(usridi ceor_953 onbeat gezaan ). done:>")

