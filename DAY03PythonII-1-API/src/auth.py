import vk

def GET_TOKEN():
    file = open("../materials/toxen.txt", "r")
    token = file.readline()
    return token
    # Допиши код
    # В файле materials/token.txt лежит токен (если такого файла нет прочти
    # информацию в materials/README.md)
    # Прочитай файл и верни токен (строка)
    
# print(GET_TOKEN())
api = vk.API(access_token=GET_TOKEN(), v='5.131')
print(api.users.get(user_ids=1))
# Выведи информацию на экран по примеру из документации
# https://vk.readthedocs.io/en/latest/usage.html#api-method-request-example
# Можешь вывести информацию о Павле Дурове либо о себе 8)
