from bs4 import BeautifulSoup
import requests
import random


# Используй функцию из прошлого задания, чтобы получить html-текст страницы согласно варианту из файла variants.md
def get_html_code(link):
    headers = {'User-Agent': "PostmanRuntime/7.32.3",
                'referer': 'https://www.google.com/'}
    # Используй функцию с прошлого задания
    res = requests.get(link, headers=headers)
    if res.ok:  # проверь результат
        return res.text
    else:
        raise RuntimeError

user_input = input('Введите режим работы: "по рабочим" или "ежедневно: "')
file = open("variants.md", "r")

listed_file = file.read().splitlines()
link = listed_file[15].split("|")[3]
# Используй ссылку и задание согласно варианту из файла materials/variants.md

# Обработай полученный текст с помощью объекта BeautifulSoap
soup = BeautifulSoup(get_html_code(link), 'html.parser')
routes =[]
routes = soup.find_all('tr', class_ = 'colorType-blue')
filtered_list =[]
for i in range(0, len(routes)):
    if user_input in str(routes[i]):
        filtered_list.append(routes[i])

# r = {str(filtered_list[i].find_all('a')).split('>')[1].split('<')[0]:str(filtered_list[i]).split('\n')[12].split('\t')[3] for i in range(0, len(filtered_list))}
# r = {filtered_list[i].find('a').contents[0]:str(filtered_list[i].find('div', class_ = 'text_with_warn')).split('\t')[3] for i in range(0, len(filtered_list))}
times = [str(filtered_list[i].find('div', class_ = 'text_with_warn')).split('\t')[3] for i in range(0, len(filtered_list))]
r = [filtered_list[i].find('a').contents[0] for i in range(0, len(filtered_list))]

print(soup.prettify())

# for i, j in r.items():
#     print(f'{i} : {j}')

for i in range(0, len(r)):
    print(f'{r[i]} : {times[i]}')
# Выведи DOM-дерево
# Изучив дерево, определи теги, необходимые для решения задачи согласно варианту


# Важно!
# Тебе могут помочь методы: find(), find_all(), unwrap() и другие
# Также почитай про parent тэг в документации BeautifulSoap 
# https://beautiful-soup-4.readthedocs.io/en/latest/
