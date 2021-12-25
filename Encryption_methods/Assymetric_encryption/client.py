import socket
import random
import pickle


def encrypt_c(mes, k):
    return [chr((ord(i) + k) % 65536) for i in mes]


def descrypt_c(mes, k):
    return [chr((65536 + (ord(i) - k) % 65536) % 65536) for i in mes]

class Cryptographer:
    def __init__(self, g=10, p=5, rand_min=1, rand_max=10):
        self.g = g
        self.p = p
        self.secret_key = random.randint(rand_min, rand_max)

    def create_open_key(self):
        """
        Создание открытого ключа
        """
        self.open_key = (self.g ** self.secret_key) % self.p
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


crypto = Cryptographer()

ip = 'localhost'
port = 9090
sock = socket.socket()
sock.connect((ip, port))
print(f'[INFO] ---\nConnect to server\nip: {ip}\nport: {port}')

sock.send(pickle.dumps(["open_key", crypto.create_open_key()]))
print(f'[INFO] Send open key: {crypto.create_open_key()}')

data = sock.recv(1024)
data = pickle.loads(data)
print(f'[INFO] Get Server open key: {data[1]}')

if data[0] == 'open_key':
    open_key = data[1]
    shared_key_client = crypto.decrypt(data[2])
print(f'[INFO] Create SharedKeyClient: {crypto.decrypt(data[2])}\n---')

while True:

    mess_out = input('>')

    (B, K) = crypto.create_shared_key(*open_key)
    data = ["", encrypt_c(encrypt_c(mess_out, shared_key_client), K), B]

    print(f'[INFO] Send cipher: {data[1]}')
    sock.send(pickle.dumps(data))
    print(f'[INFO] ---')

    if "exit" in mess_out.lower():
        sock.close()
        exit()

    data = sock.recv(1024)
    data = pickle.loads(data)

    mess_in = data[1]

    print(f'[INFO] Get message: {mess_in}')
    print(f'[INFO] Encryption')
    mess_in = 'Server: '+''.join(descrypt_c(descrypt_c(mess_in, shared_key_client), K))
    print(mess_in)
    print(f'[INFO] ---')

    if "exit" in mess_in.lower():
        sock.close()
        exit()