# Крок 2. View (відображення та взаємодія)
class OrderView:
    def show_menu(self):
        """Виводить меню користувачу [cite: 21]"""
        print("\n--- СИСТЕМА КЕРУВАННЯ ЗАМОВЛЕННЯМИ ---")
        print("1 — Додати замовлення")
        print("2 — Переглянути список замовлень")
        print("3 — Загальна сума замовлень")
        print("0 — Вихід")

    def get_input(self, prompt):
        """Зчитує введені дані [cite: 22]"""
        return input(prompt)

    def display_orders(self, orders):
        """Відображає список замовлень [cite: 23]"""
        if not orders:
            print("\nЗамовлень поки немає.")
        else:
            print("\nСписок замовлень:")
            for order in orders:
                print(f"Замовлення #{order.order_id}: {order.amount} грн")

    def display_message(self, message):
        """Відображає повідомлення та помилки [cite: 24]"""
        print(f"\n>>> {message}")