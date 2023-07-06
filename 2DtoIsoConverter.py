import os
import pygame

def converter(file):
    # Загрузка исходной текстуры для обычного tilemap
    source_texture = pygame.image.load(file)

    # Размеры исходной текстуры
    source_width = source_texture.get_width()
    source_height = source_texture.get_height()

    # Размеры изометрической текстуры (вычисляются на основе размеров исходной текстуры)
    iso_width = source_width + source_height
    iso_height = (source_width + source_height) // 2

    # Создание изометрической поверхности
    iso_texture = pygame.Surface((iso_width, iso_height), pygame.SRCALPHA)

    # Конвертация пикселей из исходной текстуры в изометрический формат
    for y in range(source_height):
        for x in range(source_width):
            source_pixel = source_texture.get_at((x, y))

            # Вычисление координаты пикселя в изометрической системе координат
            iso_x = (x - y) + source_height
            iso_y = (x + y) // 2

            # Установка пикселя на изометрической текстуре
            iso_texture.set_at((iso_x, iso_y), source_pixel)

    # Изменение размеров изометрической текстуры
    # Менять размер изображения для экспорта тут
    iso_texture = pygame.transform.scale(iso_texture, (595, 297))

    # Получение пути и имени файла без расширения
    file_path, file_name = os.path.split(file)
    file_name_without_extension = os.path.splitext(file_name)[0]

    # Создание пути для сохранения изометрической текстуры
    save_path = os.path.join(file_path,"export", file_name_without_extension + "_isometric.png")

    # Сохранение изометрической текстуры
    pygame.image.save(iso_texture, os.path.abspath(save_path))


def convert_textures_to_isometric(directory):
    # Получаем список всех файлов в указанной папке
    file_list = os.listdir(directory)

    # Проходим по каждому файлу
    for filename in file_list:
        # Проверяем, является ли файл текстурой tilemap (ваше условие)
        if filename.endswith('.png'):
            # Полный путь до файла
            file_path = os.path.join(directory, filename)

            # Выполняем преобразование
            converter(file_path)

            # Пример: выводим имя обработанного файла
            print("Обработан файл:", filename)

    print("Преобразование текстур завершено.")

# Путь до папки с текстурами (относительный путь)
folder_path = "textures"

# Вызываем функцию для преобразования текстур
convert_textures_to_isometric(folder_path)
