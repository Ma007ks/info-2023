# 234 + 196
# 214 - 149
# 42 * 133

s = input()
# s = "234 + 196"

a, op, b = s.split(" ")

a = int(a)
b = int(b)

if op == "+":
    c = a + b
elif op == "-":
    c = a - b
elif op == "*":
    c = a * b
elif op == "**":
    c = a ** b
elif op == "%":
    c = a % b
elif op == "//":
    c = a // b
elif op == "/":
    c = a / b
elif op == "@":
    c = (a ** 2 + b ** 2) ** 0.5
else:
    print("Операция неизвестна")

print(s, "=", c)
