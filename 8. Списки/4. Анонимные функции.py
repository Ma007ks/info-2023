lst = [52, 19, 87, 21, 463, 2194, 3, 10, 23418, 0, 1110]
print(lst)

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

lst.sort(key=lambda x: x % 10)
print(lst)

lst.sort(key=lambda x: x % 2)
print(lst)

lst.sort(key=lambda x: (x % 2, x))
print(lst)

# Quick Sort
