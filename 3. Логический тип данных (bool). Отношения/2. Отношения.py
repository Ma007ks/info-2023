# > — больше (строго больше)
# < — меньше (строго меньше)
# >= — не меньше (больше или равно; больше либо равно)
# <= — не больше (меньше или равно; меньше либо равно)
# == — равно (равенство семантическое)
# != — не равно
# in — входит
# not in — не входит
# is — является (равенство объектное)
# is not — не является

a, b, c, d, e, f = 1, 2, 3, 10, 5, 7
#
# print(a < b == c <= d > e < f)
# print((a < b) and (b == c) and (c <= d) and (d > e) and (e < f))
print("x" in "xyz" in "TrueTrueFalse")
print(("x" in "xyz") and ("xyz" in "TrueTrueFalse"))

print(a < b < c < d)
print(10 <= a <= 99)

# a != b ⇔ not a == b
# a >= b ⇔ not a < b
