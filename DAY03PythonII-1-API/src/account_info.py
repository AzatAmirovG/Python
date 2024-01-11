import vk
from auth import GET_TOKEN



api = vk.API(access_token=GET_TOKEN(), v='5.131')
account_info= api.account.getProfileInfo()
print(account_info)

# Выведи информацию о текущем пользователе (ФИО, дата рождения, место жительства и т.д.),
# используй авторизацию и методы, описанные в документации
# https://dev.vk.com/ru/method (<- Документация)