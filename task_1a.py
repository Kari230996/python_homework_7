'''
1. Решить задачи, которые не успели решить на семинаре.


4. Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
'''


import random
import string


def create_file(extension, min_name_length=6, max_name_length=30, min_byte=256, max_byte=4096, file_limit=42):

    counter = 0

    while counter < file_limit:
        try:
            file_name = generate_random_name(
                min_name_length, max_name_length) + '.' + extension
            with open(file_name, 'wb') as f:
                random_bytes = bytearray(random.getrandbits(
                    8) for _ in range(random.randint(min_byte, max_byte)))
                f.write(random_bytes)

            print(f'Файл {file_name} был успешно создан')
            counter += 1

        except Exception as e:
            print(
                f"Произошла ошибка при создании файла '{file_name}': {str(e)}")


def generate_random_name(min_length=6, max_length=30):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(random.randint(min_length, max_length+1)))


extension = input("Введите расширение для файлов (txt/py/....): ")
create_file(extension)
