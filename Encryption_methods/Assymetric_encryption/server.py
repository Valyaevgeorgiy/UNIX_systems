import random
import pickle
import socket
import time


def encrypt_c(mes, k):
    return [chr((ord(i) + k) % 65536) for i in mes]


def descrypt_c(mes, k):
    return [chr((65536 + (ord(i) - k) % 65536) % 65536) for i in mes]


class Cryptographer:
    def __init__(self, g=12, p=80, rand_min=1, rand_max=10):
        self.g = g
        self.p = p
        self.secret_key = random.randint(rand_min, rand_max)

    def create_open_key(self):
        """
        Создание секретного ключа
        """
        self.open_key = self.g ** self.secret_key % self.p
        return self.open_key, self.g, self.p

    def decrypt(self, B):
        """
        Получение общего секретного ключа K
        """
        return B ** self.secret_key % self.p

    def create_shared_key(self, A, g, p):
        """
        Получение внешнего открытого ключа и создание своего открытого ключа,
        а также обшего секретного
        """
        return g ** self.secret_key % p, A ** self.secret_key % p


cryptog = Cryptographer()
sock = socket.socket()

print(f'[INFO] ---\nStart Server')
ip = ''
port = 9090
sock.bind((ip, port))
print(f'[INFO] Open socket\nip: {ip}\nport: {port}')

sock.listen(1)
print(f'[INFO] Listening socket')

conn, addr = sock.accept()
print(f'[INFO] Accept new connection\nconn: {conn}\naddress: {addr}')

data = conn.recv(1024)
data = pickle.loads(data)

if data[0] == 'open_key':
    open_key = data[1]
print(f'[INFO] Get Client open key: {open_key}')

(B, K) = cryptog.create_shared_key(*open_key)

shared_key_client = K
conn.send(pickle.dumps(["open_key", cryptog.create_open_key(), B]))
print(f'[INFO] Send Servre open key: {cryptog.create_open_key()}\n---')

while True:
    data = conn.recv(1024)
    get_time = time.localtime()
    data = pickle.loads(data)

    K = cryptog.decrypt(data[2])

    mess_in = data[1]
    print(f'[INFO] Получено: {mess_in}')
    print(f'[INFO] Encryption')
    mess_in = ''.join(descrypt_c(descrypt_c(mess_in, K), shared_key_client))

    print(mess_in)
    print(f'[INFO] ---')

    if "exit" in mess_in.lower():
        conn.close()
        exit()

    mess_out = f'{time.strftime("%d %m %Y %H:%M:%S", get_time)} :: Client {addr} send message :: {mess_in}'
    data = ["message", encrypt_c(encrypt_c(mess_out, K), shared_key_client)]

    conn.send(pickle.dumps(data))
    print(f"[INFO] Send message {mess_out}\n---")

    if "exit" in mess_out.lower():
        conn.close()
        exit()
