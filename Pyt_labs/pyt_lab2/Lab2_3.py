print("Введите имя студента, затем с новой строки вводите его навыки по одному в строке.\n"
      "Для завершения ввода и перехода к другому студенту напишите пустую строку\n"
      "Для завершения ввода студентов напишите '!!!'")

data = dict()

keys = data.keys()

n = input()
while n != "!!!":
    skills = set()
    while True:
        skill = input().lower().strip()
        if not skill:
            break
        skills.add(skill)
    data[n] = skills
    n = input()

def same_skills(students, keys):
    res = list()
    names = list(keys)

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if students[names[i]] == students[names[j]]:
                res.append([names[i], names[j]])
    return res

def superset(students, keys):
    res = []

    for student_1 in keys:
        for student_2 in keys:
            if student_1 != student_2:
                if students[student_1] > students[student_2]:
                    res.append([student_1, student_2])
    return res

def max_skills(sudents, keys):
    maxi = []
    res_student = ''

    for student_1 in keys:
        if len(sudents[student_1]) > len(maxi):
            maxi = list(sudents[student_1])
            res_student = student_1

    return res_student

def jaccards_ratio(set1, set2):
    if not set1 and not set2:
        return 1.0
    return len(set1 & set2) / len(set1 | set2)

#print(same_skills(data, keys))
if same_skills(data, keys):
    print(same_skills(data, keys))
else:
    print("Нет студентов с совпадающими навыками\n")

#print(superset(data, keys))
if superset(data, keys):
    print(superset(data, keys))
else:
    print("Нет студента, чьё множество навыков является строгим подмножетсвом "
          "хотя бы одного другого студента\n")

print(f"Самое большое количество навыков у студента: {max_skills(data, keys)}\n")


print(f"{'':>8}", end = '')
for name in keys:
    print(f"{name:>10}", end = '')
print()

for name_1 in keys:
    print(f"{name_1:>8}", end = '')
    for name_2 in keys:
        ratio = jaccards_ratio(data[name_1], data[name_2])
        print(f"{ratio:>10.2f}", end = '')
    print()