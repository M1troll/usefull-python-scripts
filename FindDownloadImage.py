import requests
import os
from bs4 import BeautifulSoup
from random import choice, randint
from datetime import date


def find_image(title: str = 'котик'):
    """
    Осуществляет поиск и скачивание изображения с Интернета.

    :param title: Заголовок для поиска в Интернете.
    :return: Путь к сохраненному изображению.
    """

    title = title.lower().strip()   # для удобства приводим запрос к нижнему регистру и убираем пробелы в начале и конце

    path = f"{title.replace(' ', '_')}{randint(0,10000)}-{date.today()}.jpg"      # имя для сохранения картинки
    url = f"https://yandex.ru/images/search?text={title}"                         # путь для скачивания картинки

    # выполняем запрос в интернет
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")

    # получаем все url картинок с сайта
    images = []
    for img in soup.findAll('img'):
        images.append(img.get('src'))

    name = choice(images)   # выбираем случайную из них

    # скачиваем выбранное изображение и сохраняем в файл
    img_data = requests.get(f"https:{name}").content
    with open(path, 'wb') as handler:
        handler.write(img_data)

    # возвращаем название сохраненного файла
    return path


if __name__ == '__main__':
    query = find_image(input("Картинку с чем Вам найти: "))     # запускаем функцию поиска картинки и просим в консоли ввести запрос
    os.system(query)                                            # открываем скачанную картинку
