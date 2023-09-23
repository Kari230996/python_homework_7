'''
2. 
✔ Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

'''

import os


def rename_files(directory, desired_name, digit_count, source_extension, destination_extension, name_range):
    # Получаем список файлов в указанной директории
    files = [file for file in os.listdir(
        directory) if file.endswith(source_extension)]

    for i, file in enumerate(files):
        # Определяем диапазон символов для сохраняемой части имени файла
        start, end = name_range

        # Получаем часть имени файла в указанном диапазоне
        original_name_part = file[start-1:end]

        # Формируем порядковый номер с заданным количеством цифр
        number = str(i + 1).zfill(digit_count)

        # Создаем новое имя файла
        new_name = f"{original_name_part}{desired_name}{number}.{destination_extension}"

        # Полный путь к исходному и новому файлу
        source_path = os.path.join(directory, file)
        destination_path = os.path.join(directory, new_name)

        # Переименовываем файл
        os.rename(source_path, destination_path)


if __name__ == '__main__':
    source_directory = "source_folder"
    desired_name = "newfile"
    digit_count = 4
    source_extension = ".txt"
    destination_extension = "txt"
    name_range = (3, 6)

    # Вызываем функцию для переименования файлов
    rename_files(source_directory, desired_name, digit_count,
                 source_extension, destination_extension, name_range)
