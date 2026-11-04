from functools import reduce


def means_grades(len, students):
    means = dict()

    for student in students:
        means[student] = round(
            reduce(lambda x, a: x + a, students[student]) / len(
                students[student]), 2)
    return means


students = {'Алиса': [3, 2, 5, 5, 2, 3, 4, 3, 5, 4],
            'Степан': [4, 4, 5, 3, 5, 2, 2, 4],
            'Данил': [4, 4, 5, 2, 2, 2, 4, 5, 2, 5, 3, 4],
            'Миша': [5, 4, 3, 4, 4, 2, 2, 3, 4, 5, 3, 5],
            'Никита': [3, 5, 4, 5, 4, 2, 5, 3, 5],
            'Артём': [2, 5, 2, 4, 4, 4, 5, 5, 3, 2],
            'Дима': [5, 4, 2, 3, 3, 5, 4, 5, 5, 5, 5],
            'Андрей': [2, 4, 4, 5, 4, 4, 4, 4, 2, 5]}

print(means_grades(len, students))

# count_grades1 = sum(map(len, [students[student] for student in students]))
print(
    f"Всего оценок: {sum(map(len, [students[student] for student in students]))}")