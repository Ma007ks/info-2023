# Список (list) — это упорядоченный изменяемый набор объектов []
# Кортеж (tuple) — это упорядоченный неизменяемый набор объектов ()

# Индексы и срезы
# lst[start:finish:step] или lst[start:finish]
# — берём элементы с start до finish не включительно с шагом step
# — получаем новый список

lst = [3, 5, 7, True, "xyz"]

print(lst)
print(type(lst))
print(len(lst))

print(lst[0])
print(lst[-1])
print(lst[:3])
print(lst[-2:])
print(lst[::2])
print(lst[::-1])

lst[2] *= 2
lst[3] *= 2

lst = lst + [1, 3, 7]
lst += [5]
lst = ["первый элемент"] + lst
lst = lst + [3]
print(lst)

# # lst[:2] = [-1, -2]  # заменили первые два элемента
# lst[:2] = 1, 2, 3, 4
# # lst = [1, 2, 3, 4] + lst[2:]
#
# print(lst)
#
# print(lst[::2])
# lst[::2] = [0] * 7
# print(lst)

# lst = []

# lst = lst + [1]  # добавили в конец
# lst = [3] + lst  # добавили в начало
# lst = [2, 67, 1] + lst
# lst = lst + [4, 1, 2]

# print(lst)

# lst = [1, 2, 3, 4, 5, 6]

# lst[:len(lst) // 2] — левая половина списка
# lst[len(lst) // 2:] — правая половина списка

# lst = lst[:len(lst) // 2] + [100500] + lst[len(lst) // 2:]

# lst[2] = [lst[2], 100500]
# lst[len(lst) // 2:len(lst) // 2] = (100500,)

# print(lst)
# print(lst[3:3])
