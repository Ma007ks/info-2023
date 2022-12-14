# Приоритет операций:
# 1. Возведение в степень
# 2. Унарный минус, унарный плюс
# 3. Умножение, деления (обычное/целочисленное), взятие остатка
# 4. Сложение, вычитание
# 5. >, <, >=, <=, ==, !=, in, not in, is, is not
# 6. not
# 7. and
# 8. or

# Если операции имеют одинаковый приоритет, то они выполняются слева направо.
# Но! Исключение — возведение в степень: она выполняется справа налево
# 23 - 17 - 3 = 6 - 3 = 3

print(-3 ** 2 + 17 - 16 / 2 / 2 - 25 // 7 % 3)
print(-9 + 17 - 16 / 2 / 2 - 25 // 7 % 3)
print(-9 + 17 - 4.0 - 25 // 7 % 3)
print(-9 + 17 - 4.0 - 0)
print(8 - 4.0)
print(4.0)
