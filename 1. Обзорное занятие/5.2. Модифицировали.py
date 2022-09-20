# a, b, c = 3, 4, -7
a, b, c = 1, -2, 1

d = b ** 2 - 4 * a * c

print("Дискриминант равен", d)

if d < 0:
    print("Корней нет :с")
elif d == 0:
    x = -b / (2 * a)
    print("Один корень:", x)
else:  # d > 0
    sqrt_d = d ** 0.5  # корень из дискриминанта
    x_1 = (-b + sqrt_d) / (2 * a)
    x_2 = (-b - sqrt_d) / 2 / a
    print("Два корня:", x_1, "и", x_2)

# correct_variable_name — snake case
# correctVariableName — camel case
