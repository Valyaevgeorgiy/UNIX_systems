
def Vernam_encr(k, m):
    k = k * (len(message) // len(k)) + k[:len(message) % len(k)]
    return list(map(lambda x: x[0] ^ x[1], zip([ord(i) for i in message], [ord(i) for i in k])))

def Vernam_decr(k, c):
    k = k * (len(message) // len(k)) + k[:len(message) % len(k)]
    return ''.join([chr(i) for i in map(lambda x: x[0] ^ x[1], zip(c, [ord(i) for i in k]))])

message = "Python is very beautiful language in the world!"
key = "abc"
crypt = Vernam_encr(key, message)

print(crypt)
print()
print(Vernam_decr(key, crypt))
