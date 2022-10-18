lst = [5, 10, 17, -3, True, "hello", [2, 3, 4]]

print(lst[0])
print(lst[2])
print(lst[-1])
print(lst[-1][-2])
print([2, 3, 4][-2])
print(lst[:3])
print(lst[-1][::-1])

lst.append(5)

print(lst)

lst.remove(5)
print(lst)

print(lst.count(5))