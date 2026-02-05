from collections import deque

# 1. Реалізація черги
queue = deque()
for i in range(1, 6):
    queue.append(f"Елемент {i}")
    print(f"Додано: {queue}")

for _ in range(3):
    removed = queue.popleft() 
    print(f"Видалено {removed}: {queue}")

# 2. Симуляція черги в магазині
shop_queue = deque(["Кіра", "Дамір"])

def store_simulation():
    shop_queue.append("Марсель") 
    print(f"Прийшов клієнт. Зараз у черзі: {list(shop_queue)}")
    
    served = shop_queue.popleft() 
    print(f"Клієнт {served} обслужений. Залишились: {list(shop_queue)}")

store_simulation()