'''
Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''

import os
import shutil


def sort_files_by_category(source_directory, destination_directory):

    categories = {
        "Изображения": ['.png', '.jpg', 'jpng', '.gif'],
        "Видео": ['.avi', '.mkv', '.mp4'],
        "Текстовые": ['.txt', '.docx', '.pdf'],
        "Другие": []
    }

    for category in categories.keys():
        category_directory = os.path.join(destination_directory, category)
        os.makedirs(category_directory, exist_ok=True)

    # Перебираем все файлы в исходной директории
    for root, _, files in os.walk(source_directory):
        for file in files:
            source_path = os.path.join(root, file)

            # Определяем расширение файла
            _, extension = os.path.splitext(file)

            # Ищем категорию для даного расширения

            file_category = "Другие"

            for category, extensions in category.items():
                if extension.lower() in extensions:
                    file_category = category
                    break

            # Перемещаем файл в соответствующую поддиректорию
            destination_path = os.path.join(
                destination_directory, file_category, file)
            shutil.move(source_path, destination_path)


if __name__ == '__main__':
    source_directory = 'source_folder'
    destination_directory = "sorted_folder"

    sort_files_by_category(source_directory, destination_directory)
