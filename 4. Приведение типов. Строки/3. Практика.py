# x = 12345678  # False
# x = 1323231  # True
# x = 565  # True
# x = 1421419  # False
# x = 42915  # False
# x = 7  # True

# Проверить, является ли натуральное число x палиндромом

# print(int(str(x)[::-1]) == x)

x = 1323231
s = str(x)
print(s == s[::-1])

print(str(x) == str(x)[::-1])

# print(s)

# x = 2254
#
# print(x % 2 == 0)
#
# if x % 2 == 0:
#     print(True)
# else:
#     print(False)
