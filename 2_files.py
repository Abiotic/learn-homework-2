"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

import re


def main():
    with open('referat.txt', 'r', encoding='utf-8') as f, open('referat2.txt', 'w') as ref2:
    	file_content = f.read()
    	print(len(file_content))

    	splited_content = re.split('\n{1,}| ', file_content)
    	print(len(splited_content))

    	without_dots = file_content.replace('.','!')
    	ref2.write(without_dots)


if __name__ == "__main__":
    main()



