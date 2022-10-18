# Одинаковые ключи:
# 10, 0, 1110
# 463 и 3

# Стабильная сортировка — это сортировка, которая объекты
# с равными ключами оставляет в том же порядке

def get_last_digit(x):
    return x % 10


lst = [52, 19, 87, 21, 463, 2194, 3, 10, 23418, 0, 1110]
print(lst)


# lst.sort(key=get_last_digit)
# print(lst)


# Сначала чётные, потом нечётные: [52, 2194, 10, 23418, 0, 1110, 19, 87, 21, 463, 3]
def get_mod_2(x):
    return x % 2


# print(get_mod_2(41421))
# print(get_mod_2(412))
#
# lst.sort(key=get_mod_2)
# print(lst)


# def sort_key(x):
#     return x % 2, x
#
#
# lst.sort(key=sort_key)
# print(lst)


# Упорядочить по старшей цифре: [0, 19, 10, 1110, 21, 2194, 23418, 3, 463, 52, 87]
def get_first_digit(x):
    return int(str(x)[0])


lst.sort(key=get_first_digit)
print(lst)
