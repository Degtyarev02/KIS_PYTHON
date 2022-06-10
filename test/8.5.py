import re


def main(x):
    pattern = r'\{[\d\-\s\#\.]*'
    num_list = re.findall(pattern, x)
    num_list = list(filter(lambda val:
                           val != '{' and
                           val != '{ ' and
                           val != ', ',
                           num_list))
    for i in range(len(num_list)):
        tmp = ''.join(num_list[i])
        num_list[i] = re.findall(r'#[\-\d]*', tmp)
        num_list[i] = ''.join(num_list[i])
        num_list[i] = num_list[i].split('#')
        num_list[i] = list(filter(lambda val: val != '', num_list[i]))
        for j in range(len(num_list[i])):
            num_list[i][j] = int(num_list[i][j])

    pattern = r'\>[\w\s]*'
    word_list = re.findall(pattern, x)
    word_list = ''.join(word_list)
    word_list = word_list.split('>')
    word_list = ''.join(word_list)
    word_list = word_list.split(' ')
    word_list = list(filter(lambda val: val != '', word_list))
    result = {}
    for k in range(len(word_list)):
        result[word_list[k]] = num_list[k]
    print(result)


main(
    "\begin{{ let{#-3101 . #-493 .#5818 } => edisen_915. }}. {{ let {#-7455 . #-8261} => oresar_543.}}. {{ let {#4463 . #9022} => anrile_503. }}. \end")
