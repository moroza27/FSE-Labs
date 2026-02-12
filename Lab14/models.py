# Крок 1. Model (дані + мінімальна поведінка) 
class Order:
    """Клас, який зберігає ідентифікатор та суму замовлення [cite: 10, 11, 12]"""
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

class OrderRepository:
    """Клас, який зберігає список замовлень у пам'яті [cite: 13, 14]"""
    def __init__(self):
        self._orders = []

    def add_order(self, order):
        """Дозволяє додавати замовлення [cite: 15]"""
        self._orders.append(order)

    def get_all_orders(self):
        """Дозволяє отримати всі замовлення [cite: 16]"""
        return self._orders