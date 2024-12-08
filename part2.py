from telethon.sync import TelegramClient

api_id = 000  #Введіть ваш api_id
api_hash = ''  #Введіть ваш api_hash
name_of_group = '' #Введіть назву групи
message_destination = '' #Введіть назву групи або ім'я юзера
message_text = 'Test'
mode = 'Search' #Search якщо пошук користувачів, 'Send' при відправці повідомлень

if mode == 'Search':
    with TelegramClient('name', api_id, api_hash) as client:
        for dialog in client.iter_dialogs():
            if dialog.is_group and dialog.name == name_of_group:
                participants_list = [p.first_name for p in client.get_participants(dialog.name)]
                print('Користувачі обраної групи:', participants_list)
                break

if mode == 'Send':
    with TelegramClient('name', api_id, api_hash) as client:
        for dialog in client.iter_dialogs():
            if (dialog.is_group or dialog.is_user) and dialog.name == message_destination:
                client.send_message(dialog.entity, message_text)
                print(f'Повідомлення успішно надіслано до {message_destination}')
                break