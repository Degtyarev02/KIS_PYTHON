import re


def main(s):
    pattern = r'set[\w\s\_\d]*'
    word_list_1 = re.findall(pattern, s)
    word_list_1 = ''.join(word_list_1)
    word_list_1 = word_list_1.split('set')
    word_list_1 = ''.join(word_list_1)
    word_list_1 = word_list_1.split(' ')
    word_list_1 = list(filter(lambda val: val != '', word_list_1))

    pattern = r'\( [\w\d\_\(\)\s]*'
    word_list_2 = re.findall(pattern, s)
    for i in range(len(word_list_2)):
        pattern = r'\([\w\d\_\)]*'
        word_list_2[i] = re.findall(pattern, word_list_2[i])
        word_list_2[i] = ''.join(word_list_2[i])
        word_list_2[i] = word_list_2[i].split("(")
        word_list_2[i] = list(filter(lambda val: val != '', word_list_2[i]))
        word_list_2[i] = ''.join(word_list_2[i]).split(')')
        word_list_2[i] = list(filter(lambda val: val != '', word_list_2[i]))
    result = {}
    for j in range(len(word_list_2)):
        result[word_list_1[j]] = word_list_2[j]
    print(result)
main(
    "do do set soer_903 := array( q(lexeer_370) q(riso)). done. do set mage_183 :=array( q(anusbe) q(arve) q(ceis) ). done. end")
