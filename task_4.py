import datetime
import os

def last_operations():
    print('\n--- ПОСЛЕДНИЕ 5 ОПЕРАЦИЙ ---')

    if os.path.exists("calculator.log"):
        file = open("calculator.log", 'r')
        lines = file.readlines()
        file.close()

        if len(lines) > 0:
            start = max(0, len(lines) - 5)
            for i in range(start, len(lines)):
                print(lines[i].strip())
        else:
            print("Лог-файл пуст.")
    else:
        print("Лог-файл еще не создан.")

last_operations()

while True:
    print("\n" + "-" * 30)
    print("КАЛЬКУЛЯТОР")
    print("-" * 30)

    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        op = input("Введите операцию (+, -, *, /): ")

        if op == "+":
            result = num1 + num2
            expr = f"{num1} + {num2}"
        elif op == "-":
            result = num1 - num2
            expr = f"{num1} - {num2}"
        elif op == "*":
            result = num1 * num2
            expr = f"{num1} * {num2}"
        elif op == "/":
            if num2 == 0:
                print("Ошибка: деление на ноль!")
                continue
            result = num1 / num2
            expr = f"{num1} / {num2}"
        else:
            print("Неверная операция!")
            continue

        print(f"Результат: {expr} = {result}")

        now = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        log_line = f"{now} {expr} = {result}\n"

        file = open("calculator.log", 'a')
        file.write(log_line)
        file.close()

        print("Операция записана в лог")

    except ValueError:
        print("Ошибка: введите числа")
    except Exception as e:
        print(f"Ошибка: {e}")
