import socket
import hashlib
import json
import logging
import asyncio
from async_check_send import *
import threading

SALT = 'memkekazazaaafflolol'.encode("utf-8")  # соль для хеширования
users = []
port = 9090
adress = ['localhost', '192.168.0.101']


# Настройки логгинга
logging.basicConfig(filename="log_serv", level=logging.INFO)

with open('names.json', 'r') as file:
    names = json.load(file)


def serv_work():  
    print('Сервер работает...')

def hashpass(passw: str):  # Функция хеширования данных
    return hashlib.sha512(passw.encode("utf-8") + SALT).hexdigest()


async def main(HOST, PORT):

    server = await asyncio.start_server(listen, HOST, PORT)
    await server.serve_forever()


def name_in_base(name):  # Функция проверки имени адреса в базе

    if name not in names:
        return False
    else:
        return name

def authoriz(name, passwd):  # Функция проверки пароля

    if names[name] == hashpass(passwd):
        return True
    else:
        return False


async def listen(reader, writer):  # Основная функция работы сервера

    global users

    author = False
    addr = writer.get_extra_info('peername')

    logging.info(f"Connect - {addr}")

    senduser(writer, 'добро пожаловать! \n Введите Логин: ')

    login = await checkmsg(reader)
    check = name_in_base(login)

    if check:
        while not author:
            senduser(writer, f'Здравствуйте, {login}, Введите пароль: ')
            passw = await checkmsg(reader) 
            author = authoriz(login, passw)

    else:
        senduser(writer, f'Регистрация нового пользователя, {login}, Введите пароль:  ')
        passw = await checkmsg(reader)
        names[login] = hashpass(passw)

        with open('names.json', 'w') as file:
            json.dump(names, file)

        author = True

    users.append(writer)
    senduser(writer, 'Здесь сегодня тесновато. Но для тебя всегда место найдется!')
    
    while author:
        msg = await checkmsg(reader)
        if msg:
            sendmsg(users, login+': '+msg)

work = threading.Thread(target=serv_work)
work.start()
asyncio.run(main(adress[0], port))
