
def encrypt(mes, k):
    return [chr((ord(i) + k) % 65536) for i in mes]

def descrypt(mes, k):
    return [chr((65536 + (ord(i) - k)) % 65536) for i in mes]

print('[INFO] Шифр Цезаря')
key = int(input("key: "))

main_str = "Hello,   world!"

second_str = encrypt(main_str, key)
final_str = descrypt(second_str, key)

print(main_str, second_str, "".join(final_str))
print()

print('[INFO] Взлом шифра цезаря')
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

print(*[''.join(i) for i in list(Hack_shifr_c(second_str))], sep="\n")
