"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet
import os

ARGS1 = ['ping', 'yandex.ru']
ARGS2 = ['ping', 'youtube.com']

ya_ping = subprocess.Popen(ARGS1, stdout=subprocess.PIPE)
youtube_ping = subprocess.Popen(ARGS2, stdout=subprocess.PIPE)
for line in ya_ping.stdout:
    res = chardet.detect(line)
    print(line.decode(encoding=res['encoding']))

for line in youtube_ping.stdout:
    res = chardet.detect(line)
    print(line.decode(encoding=res['encoding']))


