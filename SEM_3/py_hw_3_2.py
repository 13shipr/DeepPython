# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

def top_10_words(text):
    count_dict = {}
    new_dict = {}
    new_text = text.replace(',', ''). \
        replace('.', ''). \
        replace('!', ''). \
        replace('?', ''). \
        replace('"', ''). \
        lower(). \
        strip()
    words_list = new_text.split()
    for word in words_list:
        counter = words_list.count(word)
        count_dict[word] = counter
    sorted_values = sorted(count_dict.values())[::-1]
    for i in sorted_values:
        for k in count_dict.keys():
            if count_dict[k] == i:
                new_dict[k] = count_dict[k]
    return list(new_dict.items())[: 10]

text = '''
Для перевода шестнадцатеричного числа в десятичное необходимо 
это число представить в виде суммы произведений степеней основания 
шестнадцатеричной системы счисления на соответствующие цифры 
в разрядах шестнадцатеричного числа.
Например, требуется перевести шестнадцатеричное число 3A5 в десятичное. 
В этом числе 3 шестнадцатеричные цифры. В соответствии с вышеуказанным 
правилом представим его в виде суммы степеней с основанием 16
'''

print(top_10_words(text))