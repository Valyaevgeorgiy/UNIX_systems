import socket
import re
from check_send import *
import threading


def printmsg():

    while True:
        try:
            data = checkmsg(sock)
            print(data)

        except (KeyboardInterrupt, ConnectionAbortedError):
            print("Соединение разорвано.")
            break


def acceptadr(adr):  # Функция проверки адреса через регулярные выражения

    if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', adr) is None:
        return False

    if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', adr).group(0) == adr:
        return adr


def acceptport(port):  # Функция проверки порта через регулярные выражения

    if re.match(r'\d{1,4}', port) is None:
        return False

    if re.match(r'\d{1,4}', port).group(0) == port:
        return port


# Список возможных адресов по умолчанию
adressation = ['localhost', '192.168.0.101']

check_add = True  # Переменные проверки адреса и порта
check_port = True

while check_add or check_port:

    adress = input("Введите адрес хоста: ((Пустая строка ввод по умолчанию)): ")
    port = input("Введите порт: ")

    if acceptadr(adress):
        check_add = False

    if acceptport(port):
        check_port = False

    if adress == "" or adress == 'localhost':
        adress = adressation[0]
        check_add = False

    if port == '':
        port = '9090'
        check_port = False

port = int(port)
sock = socket.socket()
sock.connect((adress, port))  # Подключение к серверу


ex = True
checkdata = threading.Thread(target=printmsg)
checkdata.start()

while ex:

    try:
        msg = input()
        if msg == "exit":
            ex = False
            checkdata = None
        sendmsg(sock, msg)

    except ConnectionAbortedError:
        print('Соединение закрыто.')
        break

sock.close()
