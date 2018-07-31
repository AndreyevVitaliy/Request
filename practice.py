import requests

def translate_it(file_list, result_file, lang_to='ru'):

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

    params = {
              'key': key,
              'lang': "",
              'text': ""
              }

    for k in file_list:

        lang_list = (k, lang_to)
        translate_direction = "-".join(lang_list)
        file_name = file_list[k]

        with open(file_name, "r") as file:
            file_text = file.read()
            params["text"] = file_text
            params["lang"] = translate_direction

            response = requests.get(url, params=params).json()

            with open(result_file, "a") as file1:
                file1.write("---------------{}---------------\n".format(file_name))
                file1.write(" ".join(response.get('text', [])) + "\n")
                print('Обработан файл {}'.format(file_name))
            file1.close()


file_list = {'de': 'DE.txt', 'es': 'ES.txt', 'fr': 'FR.txt'}
translate_it(file_list, "result.txt", "ru")
