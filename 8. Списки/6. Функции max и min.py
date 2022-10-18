# print(max(3, 2, 76))
# print(min(3, 2, 76))
#
# lst = [3, 6, 1, 8, 2]
# print(min(lst))
# print(max(lst))
#
# print(min("hello"))
# print(max("world"))

lst = [52, 17, 8, 419, 71, 14, 36, 49, 41, 8754, 146, 42]
print(min(lst, key=lambda x: x % 10))
print(max(lst, key=lambda x: x % 10))
