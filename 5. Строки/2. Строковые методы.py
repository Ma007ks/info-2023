s = """Я помню чудное мгновенье:
Передо мной явилась ты,
Как мимолетное виденье,
Как гений чистой красоты"""

# print(s.upper())
# print(s.lower())

# print(s.count("как"))

# x.count(y) — подсчёт числа НЕПЕРЕСЕКАЮЩИХСЯ вхождений строки y в строку x
# print("aaaaaaaaaaaaaa".count("aaa"))

# print(s.replace("Как", "Так"))

# x.replace(a, b) — заменяет ВСЕ НЕПЕРЕСЕКАЮЩИЕСЯ вхождения строки a на строку b
# Функция replace возвращает НОВУЮ строчку. Исходная остаётся нетронутой!

# print(s.replace("и", "i"))

# x = "Привет всем!"
# x = x.replace("и", "i")
# print(x)

# print(ord("☺"))
# print(chr(9486))

# print(s[s.find("Как"):])

print("xyxyxy".replace("x", "y"))
print("xyxyxy".replace("x", "y").replace("y", "x"))
print("xyxyxy".replace("x", "y").replace("y", "x").count("y"))
