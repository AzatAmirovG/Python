import vk
from auth import GET_TOKEN

api = vk.API(access_token=GET_TOKEN(), v='5.131')
friends = api.friends.get()
groups = api.groups.get()
photos = api.photos.getAll()
print(friends)
print(friends)
print(photos)

# Выведи информацию СВЯЗАННУЮ с текущим пользователем (Кол-во и список его групп, друзей. Фото и ссылки на них),
# используй авторизацию и методы, описанные в документации
# https://dev.vk.com/ru/method (<- Документация)
