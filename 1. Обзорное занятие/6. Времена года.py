m = int(input("Введите номер месяца: "))  # 1...12

if 3 <= m <= 5:  # 3 <= m and m <= 5
    print("Весна")
elif 6 <= m <= 8:
    print("Лето")
elif 9 <= m <= 11:
    print("Осень")
else:
    print("Зима")

if m in (3, 4, 5):  # 3 <= m and m <= 5
    print("Весна")
elif m in (6, 7, 8):
    print("Лето")
elif m in (9, 10, 11):
    print("Осень")
elif m in (1, 2, 12):
    print("Зима")
else:
    print("Неизвестный месяц")

# m == 1 or m == 2 or m == 12
# 1 <= m <= 2 or m == 12
# m in (1, 2, 12)
