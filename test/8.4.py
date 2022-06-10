import re

def main(x):
    pattern = r'\([\w\_\)]*'
    word_list = re.findall(pattern, x)
    pattern = r'\#[\w\d\-]*'
    num_list = re.findall(pattern, x)
    word_list = ''.join(word_list)
    word_list = word_list.split(")(")
    tmp = list(filter(lambda val: val != '', word_list[0].split('(')))
    word_list[0] = ''.join(tmp)
    tmp = list(filter(lambda val: val != '', word_list[len(word_list)-1].split(')')))
    word_list[len(word_list)-1] = ''.join(tmp)
    num_list = ''.join(num_list)
    num_list = num_list.split('#')
    num_list = list(filter(lambda val: val != '', num_list))
    result = {}
    print(word_list)
    for i in range(4):
        result[word_list[i]] = num_list[i]
    print(result)

main('[[ <data> glob q(atteor_66) <|#-8846 </data>. <data> glob q(soin) <| #4431 </data>. <data> glob q(rileri_921) <| #-6487</data>. <data> glob q(isbeso_284) <|#4416 </data>.]]')