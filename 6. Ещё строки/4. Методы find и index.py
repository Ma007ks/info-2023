s = "Привет! Как дела? Я на занятии у Ильи, мне очень нравится. Но ты ведь сам позвонил. Всё пока!"
# s = "Привет!"

# print(s.rindex(" "))
# print(s.rindex(" ", 0, 51))
# print(s[:s.rindex(" ", 0, 51)])


# Привет! Как дела? Я на занятии у Ильи, мне очень н...
if len(s) <= 50:
    print(s)
else:
    print(s[:s.rindex(" ", 0, 51)] + "...")

# find
# index
# rfind
# rindex

# print(s.find("по"))
# # print(s[74])
# # print(s[74:80])
#
# print(s.index("по"))
#
# # print(s.find("@"))
# # print(s.index("@"))
#
# print(s.rfind("по"))

# print(s[-50:])
# print(s[-50:].index("а"))
# print(s.index("а", -50))
# print(s[51])
