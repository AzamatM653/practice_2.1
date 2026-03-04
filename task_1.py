with open("text.txt", 'w') as file:
    file.write("Привет\n")
    file.write("Ford\n")
    file.write("Mustang\n")
    file.write("Motors\n")
    file.write("Пока\n")

with open("text.txt", 'r') as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

print(f"Количество строк в файле: {len(lines)}")

word_count = sum(len(line.split()) for line in lines)
print(f"Количество слов в файле: {word_count}")


longest_line = max(lines, key=len)
print(f"Самую длинную строку: {longest_line} (Длина: {len(longest_line)})")

file.close()
