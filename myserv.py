#!/usr/bin/env python
 
import socket
import os

print("---- Запуск сервера ----")
sock = socket.socket()
sock.bind(('', 9090))
print("---- Начало прослушивания порта ----")
sock.listen(1)
conn, addr = sock.accept()
print("---- Подключение клиента ----")
print()
print("----", '\t connected:', addr, "\t----")

while True: 
    while True:
        print("---- Приём данных от клиента ----")
        data = conn.recv(1024).decode()
        if not data:
            break
        print("---- Отправка порции данных ----")
        conn.send(data.upper().encode())
        if "exit".lower() in data:
            print("---- Заканчивается сеанс подключения и начинается выход ----")
            print()
            print("---- Остановка сервера ----")
            conn.close()
            os._exit(0)
