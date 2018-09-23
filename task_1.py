# Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N. Например, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()

import hashlib


def count_overlapping_substrings(s, subs):
    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        count = 0
        if h_subs == hashlib.sha1(s[i: i + len_sub].encode('utf-8')).hexdigest():
            count += 1
            return count


s_1 = input('Введите строку: ')
sum_ = 0

for i in range(len(s_1)):
    for j in range(len(s_1) + 1):
        s_2 = s_1[i: i + j]
    sum_ = sum_ + count_overlapping_substrings(s_1, s_2)

print(f'Количество различных подстрок в этой строке: {sum_}')
