# list.sort() ничего не возвращает (None)
# reverse — в каком порядке сортировать (reverse=True)

lst = [52, 19, 87, 21, 463, 2194, 3, 10, 23418, 0, 1110]

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

# key (ключ) — это функция, которая будет вызвана для каждого объекта
# и сравниваться будут результаты выполнения этой функции
# key — это обязательно функция
lst.sort(key=str)
print(lst)

lst.sort(key=bool)
print(lst)
