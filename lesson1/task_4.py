"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'администрирование', 'protocol']
for a in words:
    enc_str = a.encode('utf-8')
    dec_str = enc_str.decode('utf-8')
    print(enc_str,dec_str)


