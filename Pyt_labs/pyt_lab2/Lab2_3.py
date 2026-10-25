def same_skills(students, keys):
    res = list()
    names = list(keys)

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if students[names[i]] == students[names[j]]:
                res.append([names[i], names[j]])
    return res


def superset(students, keys):
    res = set()

    for student_1 in keys:
        for student_2 in keys:
            if student_1 != student_2:
                if students[student_1].issuperset(students[student_2]):
                    res.add(student_1)
    return res


def max_skills(students, keys):
    maxi = 0

    for student_1 in keys:
        if len(students[student_1]) > maxi:
            maxi = len(students[student_1])

    return [student for student in keys if len(students[student]) == maxi]


def jaccards_ratio(set1, set2):
    if not set1 and not set2:
        return 1.0
    return len(set1 & set2) / len(set1 | set2)


data = dict()
keys = data.keys()
n = input("Введите имя студента: ").title()

while n != "!!!":
    print("Введите его навыки по одному в строке\n"
          "Для перехода к следующему студенту введите пустую строку")
    skills = set()
    while True:
        skill = input().lower().strip()
        if not skill:
            break
        skills.add(skill)
    data[n] = skills
    n = input("Если хотите завершить ввод студентов впишите '!!!'\n"
              "Введите имя студента: ").title()

if same_skills(data, keys):
    print(f"Студенты с совпадающими навыками: {same_skills(data, keys)}")
else:
    print("Нет студентов с совпадающими навыками")

if superset(data, keys):
    print(f"Студент(ы), чьё множество навыков является строгим надмножеством "
          f"хотя бы одного студента: {superset(data, keys)}")
else:
    print("Нет студента, чьё множество навыков является строгим надмножетсвом "
          "хотя бы одного студента")

print(
    f"Самое большое количество навыков у студента: {max_skills(data, keys)}\n")

print(f"{'':>8}", end='')
for name in keys:
    print(f"{name:>10}", end='')
print()

for name_1 in keys:
    print(f"{name_1:>8}", end='')
    for name_2 in keys:
        ratio = jaccards_ratio(data[name_1], data[name_2])
        print(f"{ratio:>10.2f}", end='')
    print()
