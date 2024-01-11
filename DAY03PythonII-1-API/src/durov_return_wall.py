import vk
from auth import GET_TOKEN

api=vk.API(access_token=GET_TOKEN(), v='5.131')
wall_post = api.wall.post(message='VkAPI! #PythonProof')
wall_post_picture = api.wall.post(attachments = "photo558127308_457239017", message='vk.api')
# Опубликуй пост на своей странице
# Например, "Учу Python вместе с друзьями! VkAPI - мощь! #PythonProof"
# И второй пост, содержащий какой-либо медиа-контент (фото, гифка и др.)
# используй авторизацию и методы, описанные в документации
# https://dev.vk.com/ru/method (<- Документация)
