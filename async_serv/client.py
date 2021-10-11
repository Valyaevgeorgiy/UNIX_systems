#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()

hostname = input("Введите желаемое имя хоста (по умолчанию стоит localhost): ")
host_num = input("Введите желаемый номер порта от 1025 до 65535 (по умолчанию стоит 9090): ")
if len(hostname) == 0:
    hostname = 'localhost'
if len(host_num) == 0:
    host_num = 9090
else:
    host_num = int(host_num)


print("[INFO] ---- Начало соединения с сервером ----")
sock.connect((hostname, host_num))
print("[INFO] ---- Подключение к серверу успешно пройдено ----")

while True:
    print("[INFO] ---- Начало ожидания порции данных на сервере ----")
    word = input()
    print("[INFO] ---- Отправка данных на сервер ----")
    if word == "":
        word = "exit"
    sock.send(word.encode())
    data = sock.recv(1024).decode()
    if "EXIT" in data:
        print("[INFO] ---- Разрыв соединения с сервером ----")
        sock.close()
        break
    print("[INFO] ---- Приём данных от сервера ----")
    print()
    print(data)

