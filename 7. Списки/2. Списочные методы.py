lst = []

# lst.append(x) добавляется новый элемент x в конец списка lst

lst.append(5)
lst.append(3)
lst.append(10)
lst.append(17)
print(lst)

# lst.insert(index, object): вставляет элемент object на позицию index,
# элементы при этом сдвигаются
lst.insert(0, -1000)
print(lst)

lst.insert(2, 666)
print(lst)

middle = len(lst) // 2
lst.insert(middle, 100)
print(lst)

lst.insert(-1, -13)
lst.append(666)
print(lst)

# lst.count(x) возвращает количество вхождений элемента x в список
print(lst.count(666))

# lst.remove(x) удаляет первое вхождение элемента x в списке
lst.remove(666)
print(lst)

# lst.clear() очищает список (удаляет из него все элементы)
lst.clear()

lst = [2, 3, 4, 3, 2, 3, 4, 5]
# print(lst)

# lst.index(x, start, stop) возвращает индекс первого вхождения
# элемента x в список
print(lst.index(3, 2))

print(lst)
lst.reverse()
# lst = lst[::-1]

print(lst)

lst.sort()
lst.reverse()

# print(lst)
