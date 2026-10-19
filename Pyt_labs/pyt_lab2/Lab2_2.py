def friends(names, keys):
    for person_1 in list(keys):
        for person_2 in list(keys):
            if len(names[person_1] & names[person_2]) >= 2:
                return [person_1, person_2]


print(
    "Введите имена друзей через ---: (друг1 --- друг2). "
    "Для окончания ввода напишите '!!!'")
persons = dict()
keys = persons.keys()
n = input()

while n != "!!!":
    name1, name2 = n.split(" --- ")
    if name1 in keys:
        persons[name1].add(name2)
    else:
        persons[name1] = persons.get(name1, {name2})
    if name2 in keys:
        persons[name2].add(name1)
    else:
        persons[name2] = persons.get(name2, {name1})
    n = input()

friend_1, friend_2 = friends(persons, keys)
print(f"{friend_1} - {friend_2}")
