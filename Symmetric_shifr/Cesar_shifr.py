
def enc_desc(k, m):
    return ''.join(map(chr, [x ^ k for x in map(ord, m)]))

def encrypt_2(mes, k):
    return [chr((ord(i) + k) % 65536) for i in mes]

def descrypt_2(mes, k):
    return [chr((65536 + (ord(i) - k)) % 65536) for i in mes]

key = int(input("key: "))

main_str = "Hello,   world!"

second_str = enc_desc(key, main_str)

second_2_str = encrypt_2(main_str, key)

final_str = enc_desc(key, second_str)

print(second_str, final_str, sep="\n")
print()

def Hack_shifr_c(mes):

    numdict = {}

    for i in set(mes):
        numdict[i] = mes.count(i)

    max_symb = max(numdict.values())

    plist = []

    for k, v in numdict.items():
        if v == max_symb:
            plist.append(k)

    for ch in plist:
        yield [chr((65536 + ord(i) - (ord(ch) - ord(" "))) % 65536) for i in mes]

print(*list(Hack_shifr_c(second_2_str)))