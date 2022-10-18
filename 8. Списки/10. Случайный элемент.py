from random import shuffle, randint, choice, choices

# lst = [4, 12, 7, 2, 4, 5, 6, 7]
# shuffle(lst)
# print(lst)
# shuffle(lst)
# print(lst)

# x = randint(5, 10)
# print(x)

# print(choice(lst))
# print(choices(lst, k=2))

from random import choice

lst = ["Aмелия", "Арслан", "Даниил", "Дима", "Кирилл", "Костя", "Ксюша", "Макар", "Самир", "Слава Горшков",
       "Слава Тарасов"]

while lst:
    person = choice(lst)
    lst.remove(person)
    print(person, "— умничка и зайка")
