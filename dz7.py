def main(hexdata):
    decimal = int(hexdata, 16)  # Переводим шестнадцатеричное число в десятичное
    result = 0  # Результирующая переменная

    for i in range(16):
        bit = decimal & 1  # Определялкм бит,который равен 1 (см двоично-десятичную EC)
        result |= bit << i   # "складываем" биты из CHAO: 01110101
        decimal >>= 1

    return result


print(main('0xe427a6'))
print(main('0x3f7d274'))
print(main('0x157a905'))
print(main('0x3aa1f2b'))
