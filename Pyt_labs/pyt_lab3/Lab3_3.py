import re


# Кодирование строки в вид: буква, количество букв подрят
def coder(string):
    pattern = r'([a-zA-Z])\1*'
    res_string = ''

    for x in re.finditer(pattern, string):
        res_string += x.group(1) + str(len(x.group(0)))
    return res_string


# Декодирование строки в изначальную
def decoder(cod_string):
    decod_pattern = r'([a-zA-Z])(\d+)'
    res_string = ''

    for x in re.finditer(decod_pattern, cod_string):
        res_string += x.group(1) * int(x.group(2))
    return res_string


# Ввод строки пользователем
while True:
    input_string = input("Введите строку для закодирования:\n")
    if input_string:
        break
    else:
        print("Введите строку!")

print(f"<<{decoder(coder(input_string))}>> -> <<{coder(input_string)}>>")
# print(re.sub(pattern, lambda m: m.group(1) + str(len(m.group(0))), string))

if decoder(coder(input_string)) == input_string:
    print(True)