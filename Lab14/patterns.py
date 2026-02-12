from abc import ABC, abstractmethod
import time

# Завдання 2. Strategy (Розрахунок ціни)
class IPriceStrategy(ABC):
    @abstractmethod
    def calculate(self, price):
        pass

class NormalPrice(IPriceStrategy):
    """Без знижки [cite: 46]"""
    def calculate(self, price):
        return price

class RegularCustomerDiscount(IPriceStrategy):
    """Зі знижкою для постійного клієнта [cite: 47]"""
    def calculate(self, price):
        return price * 0.9  # 10% знижки

class BulkOrderDiscount(IPriceStrategy):
    """Зі знижкою для великого замовлення [cite: 48]"""
    def calculate(self, price):
        return price * 0.8  # 20% знижки

# Завдання 4. Decorator (Розширення поведінки) [cite: 70, 77]
class OrderServiceBase(ABC):
    @abstractmethod
    def process(self):
        pass

class BaseOrderService(OrderServiceBase):
    def process(self):
        print("Обробка замовлення в базовому сервісі...")

class LoggingDecorator(OrderServiceBase):
    """Додає логування [cite: 73, 79]"""
    def __init__(self, service):
        self._service = service

    def process(self):
        print("[LOG]: Початок операції...")
        self._service.process()
        print("[LOG]: Операція завершена.")

class TimerDecorator(OrderServiceBase):
    """Вимірювання часу виконання [cite: 74, 82]"""
    def __init__(self, service):
        self._service = service

    def process(self):
        start = time.time()
        self._service.process()
        end = time.time()
        print(f"[TIMER]: Час виконання: {end - start:.4f} сек")