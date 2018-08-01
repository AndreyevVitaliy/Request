import requests
import os


def translate_it(file_text, file_language, translate_language = "ru"):

    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20180730T160327Z.75884684ebb96a11.f88c6ab69428da7e35b9412a3af2a25c3df3035b'

    lang_list = (file_language, translate_language)
    translate_direction = "-".join(lang_list)

    params = {
              'key': key,
              'lang': translate_direction,
              'text': file_text
              }

    response = requests.get(url, params=params).json()


    return " ".join(response.get('text', [])) + "\n"

def get_text_files():

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_list = list()

    for file in os.listdir(current_dir):
        if file == "result_1.txt":
            continue
        if file.endswith(".txt"):

            file_list.append(file)


    return file_list


def read_file(file_name):

    with open(file_name, "r") as file:
        file_text = file.read()

    return file_text

def write_file(file_name, translate_result):

    with open(file_name, "a") as file1:
        file1.write(translate_result)


file_list = get_text_files()

for file in file_list:
    text_file = read_file(file)

    translate_result = translate_it(text_file, "de")
    write_file("result_1.txt", translate_result)
    print("Переведен файл {}.".format(file))

print("Перевод всех файлов завершен!")

