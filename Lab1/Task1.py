list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел
list_ = set(list_)
sum_unique = sum(list_)
len_unique = len(list_)
arithmetic_mean_unique = round(sum_unique/len_unique, 5)

print(sum_unique)
print(len_unique)
print(arithmetic_mean_unique)
