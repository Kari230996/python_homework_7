'''
Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.

'''

import random
import string

def create_file(extension, min_name_length=6, max_name_length=30, min_byte=256, max_byte=4096, file_limit=3):
    counter = 0

    while counter < file_limit:
        try:
            file_name = generate_random_name(min_name_length, max_name_length) + '.' + extension
            with open(file_name, 'wb') as f:
                random_bytes = bytearray(random.getrandbits(8) for _ in range(random.randint(min_byte, max_byte)))
                f.write(random_bytes)

            print(f'Файл {file_name} был успешно создан')
            counter += 1

        except Exception as e:
            print(f"Произошла ошибка при создании файла '{file_name}': {str(e)}")

def generate_random_name(min_length=6, max_length=30):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(random.randint(min_length, max_length+1)))

def generate_files_with_extensions(extensions_and_counts):
    for extension, count in extensions_and_counts:
        for _ in range(count):
            create_file(extension)

# Пример использования:
extensions_and_counts = [("txt", 2), ("py", 3), ("jpg", 1)]
generate_files_with_extensions(extensions_and_counts)
