#!/usr/bin/env python
 
import socket
import os

print("[INFO] ---- Запуск сервера ----")

sock = socket.socket()
serv_adr = ('', 9090)

sock.bind(serv_adr)

print(f"[INFO] ---- Начало прослушивания порта {serv_adr[1]} на localhost ----")

sock.listen(1)
print("[INFO] ---- Подключение клиента ----")
print()

conn, adr = sock.accept()

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
            break
    if ("exit".lower() in data) or not data:
        print()
        print("[INFO] ---- Остановка сервера ----")
        break
conn.close()