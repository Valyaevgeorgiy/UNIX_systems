#!/usr/bin/env python
 
import socket
import os

print("[INFO] ---- Запуск сервера ----")

sock = socket.socket()
sock.bind(('', host_num))

print("[INFO] ---- Начало прослушивания порта ----")

sock.listen(1)
conn, adr = sock.accept()

print("[INFO] ---- Подключение клиента ----")
print()
print("[INFO] ----", '\t Установлено соединение с IP', adr, "\t----")

while True: 
    while True:
        print("[INFO] ---- Приём данных от клиента ----")

        data = conn.recv(1024).decode()

        if not data:
            break

        print()
        print("[INFO] ---- Отправка порции данных ----")
        conn.send(data.upper().encode())

        if "exit".lower() in data:
            print("[INFO] ---- Заканчивается сеанс подключения и начинается выход ----")
            print()
            print("[INFO] ---- Остановка сервера ----")
            conn.close()
            os._exit(0)