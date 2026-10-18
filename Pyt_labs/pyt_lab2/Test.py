lst = dict()
keys = lst.keys()
n = input()
while n != "!!!":
    key, value = n.split(" --- ")
    if key in keys:
        lst[key].add(value)
        lst[value].add(key)
    else:
        lst[key] = lst.get(key, {value})
        lst[value] = lst.get(value, {key})
    print(lst)
    print(keys)
    n = input()

print(lst)
for person_1 in list(keys):
    for person_2 in list(keys):
        if len(lst[person_1] - lst[person_2]):
            print(f"{person_1} - {person_2}")
