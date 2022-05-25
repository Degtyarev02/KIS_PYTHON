def main(tabl):
    parsed = set()
    result = []
    for name, num, email in tabl:
        parsed_res = []
        if name is None:
            continue

        name_list = name.split(' ')
        name_tmp = name_list[1]
        name_list[1] = name_list[0]
        name_list[0] = name_tmp
        parsed_res.append(' '.join(name_list))
        parsed_res.append(str(format(float(num), '.4f')))
        parsed_res.append(email.replace('[at]', '@'))
        if parsed_res not in result:
            result.append(parsed_res)
    return \
        [[result[j][i] for j in range(len(result))]
         for i in range(len(result[0]))]


table = [

    ['Марк Кениди', '0.72', 'kenidi95[at]yandex.ru', ],
    ['Марк Кениди', '0.72', 'kenidi95[at]yandex.ru', ],
    ['Виктор Сазов', '0.58', 'viktor80[at]rambler.ru', ],
    [None, None, None]
]

print(main(table))
