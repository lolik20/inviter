from telethon.sync import TelegramClient
from telethon import functions, types
import time
from telethon.tl.functions.channels import InviteToChannelRequest
# Указываем параметры авторизации
api_id = 21669282  # Вставить свой API ID
api_hash = '296682a49e5d8a71a7e30a69cbffc78b'  # Вставить свой API Hash
users = []
filename = "users.txt"

# Читаем список пользователей из файла
with open(filename, "r") as file:
    users = [line.strip() for line in file]

# Создаем сессию клиента и подключаемся к Telegram API
with TelegramClient('session_name', api_id, api_hash) as client:
    # Идентификатор группы, в которую будем приглашать пользователей
    group_id = "https://t.me/segagameclubchat"
    
    # Перебираем список пользователей и приглашаем их в группу
    for user in users:
        try:
            # Получаем идентификатор пользователя по юзернейму
            user_entity = client.get_entity(user)
            
            # Приглашаем пользователя в группу
            client(InviteToChannelRequest(channel=group_id, users=[user_entity]))
            print(f"Пользователь {user} приглашен в группу {group_id}")
            time.sleep(600)
        except Exception as e:
            print(f"Ошибка при приглашении пользователя {user}: {e}")
