from models import Order, OrderRepository
from views import OrderView
from patterns import NormalPrice, RegularCustomerDiscount, LoggingDecorator, BaseOrderService

# Крок 3. Controller (координація)
class OrderController:
    def __init__(self, model: OrderRepository, view: OrderView):
        self.model = model
        self.view = view

    def add_order_logic(self):
        """Отримує команди від View та викликає методи Model [cite: 29]"""
        try:
            order_id = self.view.get_input("Введіть ID замовлення: ")
            base_amount = float(self.view.get_input("Введіть суму: "))
            
            # Демонстрація Strategy: вибір ціни (наприклад, 10% знижки)
            strategy = RegularCustomerDiscount()
            final_amount = strategy.calculate(base_amount)
            
            new_order = Order(order_id, final_amount)
            self.model.add_order(new_order)
            self.view.display_message(f"Замовлення додано (з урахуванням знижки: {final_amount} грн)")
        except ValueError:
            self.view.display_message("Помилка: сума повинна бути числом!")

    def show_all(self):
        orders = self.model.get_all_orders()
        self.view.display_orders(orders)

    def show_total(self):
        orders = self.model.get_all_orders()
        # Перегляд загальної суми всіх замовлень [cite: 8]
        total = sum(o.amount for o in orders)
        self.view.display_message(f"Загальна сума всіх замовлень: {total} грн")

    def run(self):
        """Реалізувати цикл роботи програми [cite: 30, 31]"""
        # Демонстрація Decorator при запуску [cite: 82]
        service = LoggingDecorator(BaseOrderService())
        service.process()

        while True:
            self.view.show_menu()
            choice = self.view.get_input("Виберіть дію: ")
            
            if choice == "1":
                self.add_order_logic()
            elif choice == "2":
                self.show_all()
            elif choice == "3":
                self.show_total()
            elif choice == "0":
                print("Вихід...")
                break
            else:
                self.view.display_message("Невірний вибір!")

if __name__ == "__main__":
    model = OrderRepository()
    view = OrderView()
    controller = OrderController(model, view)
    controller.run()