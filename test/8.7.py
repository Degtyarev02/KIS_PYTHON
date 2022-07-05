import re


def main(s):
    pattern = r'make[\w\d\_\s]*'
    word_list = re.findall(pattern, s)
    word_list = list(filter(lambda val: val != ' ' and val != ',', word_list))
    word_list = ''.join(word_list)
    word_list = word_list.split(" ")
    word_list = list(filter(lambda val: val != 'make', word_list))

    pattern = r'\{[\d\s\-]*'
    num_list = re.findall(pattern, s)
    num_list = list(filter(lambda val: val != '{ ' and val != ', ', num_list))
    num_list = ''.join(num_list)
    num_list = num_list.split('{')
    num_list = list(filter(lambda val: val != '', num_list))
    for i in range(len(num_list)):
        num_list[i] = num_list[i].split(' ')
        num_list[i] = list(filter(lambda val: val != '', num_list[i]))
    result = {}
    for j in range(len(num_list)):
        result[word_list[j]] = num_list[j]
    print(result)


main(
    "{ <<make bece_692 :{ -1623 -1202 }>>, << make erzaat_509 :{7029 1646 -841 } >>, <<make onus: { -3357 -9883 -5039}>>, }")
