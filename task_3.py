file = open("products.csv", 'w')
file.write("Название,Цена,Количество\n")
file.write("Яблоки,100,50\n")
file.write("Бананы,80,30\n")
file.write("Молоко,120,20\n")
file.write("Хлеб,40,100\n")
file.close()

print("=" * 50)

# ГЛАВНОЕ МЕНЮ ПРОГРАММЫ
while True:
    print("\n--- МЕНЮ ПРОГРАММЫ ---")
    print("1. Показать все товары")
    print("2. Добавить новый товар")
    print("3. Найти товар по названию")
    print("4. Посчитать общую стоимость склада")
    print("5. Выйти")

    choice = input("Выберите действие (1-5): ")

    if choice == "1":

        file = open("products.csv", 'r')
        lines = file.readlines()
        file.close()

        print("\n--- ВСЕ ТОВАРЫ ---")
        for line in lines:
            print(line.strip())

    elif choice == "2":
        print("\n--- ДОБАВЛЕНИЕ ТОВАРА ---")
        name = input("Введите название товара: ")
        price = input("Введите цену: ")
        quantity = input("Введите количество: ")

        file = open("products.csv", 'a')
        file.write(f"{name},{price},{quantity}\n")
        file.close()

        print(f"Товар {name} добавлен")

    elif choice == "3":
        print("\n--- ПОИСК ТОВАРА ---")
        search_name = input("Введите название товара для поиска: ")

        file = open("products.csv", 'r')
        lines = file.readlines()
        file.close()

        found = False
        for line in lines[1:]:
            if search_name.lower() in line.lower().split(',')[0]:
                print(f"Найден: {line.strip()}")
                found = True

        if not found:
            print("Товар не найден")

    elif choice == "4":

        print("\n--- ОБЩАЯ СТОИМОСТЬ  ---")

        file = open("products.csv", 'r')
        lines = file.readlines()
        file.close()

        total = 0
        for line in lines[1:]:
            parts = line.strip().split(',')
            name = parts[0]
            price = int(parts[1])
            q = int(parts[2])

            item_total = price * q
            total = total + item_total

            print(f"{name}: {price} руб * {q} шт = {item_total} руб")

        print(f"\nСумма: {total} руб")

    elif choice == "5":
        print("Программа завершена")
        break

    else:
        print("Неверный выбор, Введите число от 1 до 5")