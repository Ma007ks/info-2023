lst = [1, 2, 3]

# lst += [5, 6]
# lst += "hello"
lst.extend([5, 6])
lst.extend("hello")

lst.append([5, 6])
lst.append("hello")

print(lst)
