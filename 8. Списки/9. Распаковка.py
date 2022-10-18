# lst = [4, 2, 1, 5]
# x, y, *z = lst
# print(x)
# print(y)
# print(z)

# lst = [2, 6]
# x, *lst, y = lst
# print(x, y, lst)

a = [1, 6, 2, 87]
b = [4, 2, 7, 8]
c = "Hello"

# lst = a + b + list(c)
# lst = [a, b, c]
# lst = [*a, *b, *c]
# print(lst)

print(a)
print(*a, *b, *c, sep=":")
