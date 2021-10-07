#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
print("---- Начало соединения с сервером ----")
sock.connect(('localhost', 9090))

while True:
    print("---- Подключение к серверу успешно пройдено ----")
    print("---- Начало ожидания порции данных на сервере ----")
    word = input()
    print("---- Отправка данных на сервер ----")
    sock.send(word.encode())
    data = sock.recv(1024).decode()
    if "EXIT" in data:
        print("---- Разрыв соединения с сервером ----")
        sock.close()
        break
    print("---- Приём данных от сервера ----")
    print()
    print(data)
