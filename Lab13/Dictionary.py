# 1. Базовий словник
student = {
    "ім’я": "Аліна",
    "дані": (17, "ІПЗ-3/2")
}
print(f"Старт: {student}")

student["місто"] = "Київ"
print(f"Додано місто: {list(student.keys())}, {list(student.values())}")

student["ім’я"] = "Катерина" 
print(f"Змінено ім'я: {list(student.keys())}, {list(student.values())}")

del student["дані"] 
print(f"Після видалення: {list(student.keys())}, {list(student.values())}")

# 2. Оновлення даних (Підрахунок оцінок)
marks = [5, 4, 5, 3, 4, 5, 3]
stats = {}
for m in marks:
    if m in stats:
        stats[m] += 1
    else:
        stats[m] = 1
print(f"Статистика оцінок: {stats}")

# 3. Меню магазину
inventory = {
    "Хліб": 25.50,
    "Молоко": 38.00,
    "Яблука": 45.00
}

def menu():
    while True:
        print("\n--- МЕНЮ МАГАЗИНУ ---")
        print("1 — Додати товар")
        print("2 — Видалити товар")
        print("3 — Показати всі товари")
        print("0 — Вихід")
        
        choice = input("Ваш вибір: ")
        
        if choice == "1":
            name = input("Введіть назву товару: ").capitalize()
            price = float(input(f"Введіть ціну для '{name}': "))
            inventory[name] = price
            print(f"Товар '{name}' додано/оновлено.")

        elif choice == "2":
            name = input("Який товар видалити?: ").capitalize()
            # Метод pop видаляє і повертає значення, або None, якщо ключа немає
            removed_item = inventory.pop(name, None)
            if removed_item:
                print(f"Товар '{name}' видалено.")
            else:
                print(f"Помилка: товару '{name}' немає в наявності.")

        elif choice == "3":
            if not inventory:
                print("Магазин порожній.")
            else:
                print("\nПоточний асортимент:")
                for name, price in inventory.items():
                    print(f"- {name}: {price} грн")
        
        elif choice == "0":
            print("Вихід з програми. Гарного дня!")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз.")

menu()