file = open("students.txt", 'w')
file.write("Иванов Иван:5,4,3,5\n")
file.write("Петров Петр:4,3,4,4\n")
file.write("Сидорова Мария:5,5,5,5\n")
file.close()


file = open("students.txt", 'r')
lines = file.readlines()
file.close()

names = []
averages = []

for line in lines:
    line = line.strip()

    parts = line.split(':')
    name = parts[0]
    grades_str = parts[1]

    grades_list = grades_str.split(',')

    grade_1 = int(grades_list[0])
    grade_2 = int(grades_list[1])
    grade_3 = int(grades_list[2])
    grade_4 = int(grades_list[3])

    summa = grade_1 + grade_2 + grade_3 + grade_4
    avg = summa / 4

    names.append(name)
    averages.append(avg)

    print(f"{name} - средний балл: {avg}")

file = open("result.txt", 'w')
file.write("Студенты со средним баллом выше 4.0:\n")

for i in range(len(names)):
    if averages[i] > 4.0:
        file.write(f"{names[i]} - {averages[i]}\n")

file.close()

best_index = 0
best_avg = averages[0]

for i in range(len(averages)):
    if averages[i] > best_avg:
        best_avg = averages[i]
        best_index = i

print("\nСтудент с наивысшим баллом:")
print(f"{names[best_index]} со средним баллом {averages[best_index]}")