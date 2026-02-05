# Завдання 1

numbers = [12, 5, 8, 24, 1, 15, 7, 33, 19, 10]

# Функція для пошуку мінімуму та максимуму
def find_min_max(lst):
    mn = lst[0]
    mx = lst[0]
    for x in lst:
        if x < mn: mn = x
        if x > mx: mx = x
    return (mn, mx)  # Повертаємо кортеж

# Функція для обчислення суми
def calculate_sum(lst):
    total = 0
    for x in lst:
        total += x
    return total

# Функція для середнього арифметичного
def calculate_average(lst):
    total = calculate_sum(lst)
    count = 0
    for _ in lst:
        count += 1
    return total / count

min_max = find_min_max(numbers)
total_sum = calculate_sum(numbers)
avg = calculate_average(numbers)

print(f"Мін/Мак: {min_max}, Сума: {total_sum}, Середнє: {avg}")

# Завдання 2

data = [[1, 4, 7], [2, 5], [9, 3, 6, 8]]

def flatten_list(nested_list):
    flat = []
    for sublist in nested_list:
        for item in sublist:
            flat.append(item)
    return flat

flat_data = flatten_list(data)
flat_data.sort()  # Сортування за зростанням
print(f"Відсортований список: {flat_data}")

# Завдання 3

students = [
    ("Роман", 81),
    ("Аліна", 95),
    ("Дарина", 73),
    ("Оля", 92)
]

# Пошук найкращого студента
def get_best_student(student_list):
    best = student_list[0]
    for s in student_list:
        if s[1] > best[1]:  # Порівнюємо оцінки (індекс 1)
            best = s
    return best

# Список лише з оцінками
def get_only_grades(student_list):
    grades = []
    for s in student_list:
        grades.append(s[1])
    return grades

# Кількість студентів з оцінкою вище заданої
def count_above_limit(student_list, limit):
    count = 0
    for s in student_list:
        if s[1] > limit:
            count += 1
    return count

# Результати
best_student = get_best_student(students)
all_grades = get_only_grades(students)
above_80 = count_above_limit(students, 80)

print(f"Найкращий: {best_student}")
print(f"Усі оцінки: {all_grades}")
print(f"Студентів з балом > 80: {above_80}")