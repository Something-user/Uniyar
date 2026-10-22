from functools import reduce

def means_grades(len1, students):
    means = dict()

    for student in students:
        means[student] = round(
            reduce(lambda x, a: a + x, students[student]) / len1(
                students[student]), 2)
    return means

def len1(grades):
    student_grades = grades.copy()
    count = 0
    while student_grades:
        count += 1
        student_grades.pop()

    return count


data = {'Алиса': [4, 2, 3, 2, 4, 3, 3, 2, 4, 4],
        'Степан': [5, 4, 4, 3, 5, 3, 4, 4, 5, 3],
        'Данил': [3, 5, 3, 2, 5, 2, 5, 4, 2, 2],
        'Миша': [4, 2, 2, 3, 3, 2, 2, 4, 5, 3],
        'Никита': [4, 2, 5, 2, 5, 2, 4, 3, 4, 3],
        'Артём': [3, 4, 5, 5, 4, 4, 5, 2, 3, 3],
        'Дима': [2, 2, 5, 4, 2, 2, 2, 2, 4, 4],
        'Андрей': [5, 5, 2, 4, 3, 5, 4, 4, 3, 3]}

students = {'Алиса': [3, 2, 5, 5, 2, 3, 4, 3, 5, 4],
         'Степан': [4, 4, 5, 3, 5, 2, 2, 4],
         'Данил': [4, 4, 5, 2, 2, 2, 4, 5, 2, 5, 3, 4],
         'Миша': [5, 4, 3, 4, 4, 2, 2, 3, 4, 5, 3, 5],
         'Никита': [3, 5, 4, 5, 4, 2, 5, 3, 5],
         'Артём': [2, 5, 2, 2, 4, 4, 5, 5, 3, 2],
         'Дима': [5, 4, 2, 3, 3, 5, 4, 5, 5, 5, 5],
         'Андрей': [2, 4, 2, 3, 4, 4, 4, 4, 2, 5]}



print(means_grades(len1, students))

count_grades = 0
for student in students:
    count_grades += len(students[student])

print(f"Всего оценок: {count_grades}")

for student in students:
    print(len1(students[student]), end = " ")
