def get_count_char(str_):
    str_ = "".join(sorted(str_.lower().split()))
    dict_elem = {}
    for elem in str_:
        if elem.isalpha():
            dict_elem[elem] = str_.count(elem)
    return dict_elem


def get_percentage(dict_element):
    for i in dict_element:
        dict_element[i] = round(dict_element[i] / len(main_str) * 100, 2)
    return dict_element

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

count_char = get_count_char(main_str)
print(count_char)
percentage = get_percentage(count_char)
print(percentage)