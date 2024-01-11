import requests
import random

# Допиши код
# Напиши get-запрос (HTTP GET) с использование ссылки (link) согласно варианту из файла materials/variants.md
# Проверь, что запрос вернул код OK
# И верни html-текст
# Если вернулась ошибка (не OK), то сообщи об этом пользователю и вызови ошибку (raise RuntimeError)
def get_html_code(link):
    # Это поможет тебе избежать некоторых ошибок
    headers = {'User-Agent': "PostmanRuntime/7.32.3",
                'referer': 'https://www.google.com/'}
    # Вызывай get запрос с параметром headers=headers
    # for i in link:
    res = requests.get(link, headers=headers)
    if res.ok:  # проверь результат
        return res.text
    else:
        raise RuntimeError
            

file = open("variants.md", "r")
listed_file = file.read().splitlines()
# link = [i.split("|")[3] for i in listed_file[2:]]
link = listed_file[random.randint(2, sum(1 for line in listed_file ))].split("|")[3]

print(get_html_code(link))
