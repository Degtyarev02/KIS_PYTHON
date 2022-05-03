def main(tabl):
    parsed = set()
    result = []
    for num, email, data in tabl:
        parsed_res = []
        if data in parsed or data is None:
            continue
        name = data.split('!')[1]
        name = name.split(' ')[1]
        telephone = data.split('!')[0]
        parsed_res.append(str(round(float(num), 1)))
        parsed_res.append(email.split('@')[0])
        phone1 = telephone.replace(' ', '').replace('-', '').split(' ')
        phone = ''.join(phone1)
        parsed_res.append(phone)
        parsed_res.append(name)
        if parsed_res not in result:
            result.append(parsed_res)
    return \
        [[result[j][i] for j in range(len(result))]
         for i in range(len(result[0]))]


table = [
    ['0.3897', 'aleksandr23@yahoo.com', '841 592-5650!Александр Кокук'],
    ['0.9116', 'kenidi95@yandex.ru', '502 418-5203!Марк Кениди'],
    ['0.9116', 'kenidi95@yandex.ru', '502 418-5203!Марк Кениди'],
    [None, None, None],
    ['0.1727', 'mozskij5@yahoo.com', '087 052-6716!Филипп Моцский'],
    ['0.9116', 'kenidi95@yandex.ru', '502 418-5203!Марк Кениди'],
    ['0.4807', 'matvej49@gmail.com', '879 295-3887!Матвей Медев'],
]

print(main(table))
