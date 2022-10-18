# def sm(x, y, z=0):
#     return x + y + z
# print(sm(5, 3))


def my_sum(*args):
    return sum(args)


print(my_sum(3, 21, 7))
print(my_sum(7, 2, 10))
