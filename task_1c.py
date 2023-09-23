'''
Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён
'''

import random
import string
import os
from pathlib import Path


def create_file(extension, directory, min_name_length=6, max_name_length=30, min_byte=256, max_byte=4096, file_limit=3):
    counter = 0

    # Создаем директорию, если она не существует
    Path(directory).mkdir(parents=True, exist_ok=True)

    while counter < file_limit:
        try:
            file_name = generate_random_name(
                min_name_length, max_name_length) + '.' + extension
            file_path = os.path.join(directory, file_name)

            # Проверяем, существует ли уже файл с таким именем
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    random_bytes = bytearray(random.getrandbits(
                        8) for _ in range(random.randint(min_byte, max_byte)))
                    f.write(random_bytes)

                print(
                    f'Файл {file_name} был успешно создан в директории {directory}')
                counter += 1
            else:
                print(
                    f'Файл {file_name} уже существует в директории {directory}, пропускаем его создание')

        except Exception as e:
            print(
                f"Произошла ошибка при создании файла '{file_name}': {str(e)}")


def generate_random_name(min_length=6, max_length=30):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(random.randint(min_length, max_length+1)))


def generate_files_with_extensions(extensions_and_counts, directory):
    for extension, count in extensions_and_counts:
        for _ in range(count):
            create_file(extension, directory)


# Пример использования:
extensions_and_counts = [("txt", 2), ("py", 3), ("jpg", 1)]
directory = "my_directory"
generate_files_with_extensions(extensions_and_counts, directory)
