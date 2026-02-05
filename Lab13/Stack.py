# 1. Реалізація та базові операції
stack = [] 
for i in range(1, 6):
    stack.append(i) 
stack.pop() 
stack.pop()
print(f"Поточний стек: {stack}")

# 2. Функція перевірки порожності
def is_empty(s):
    return len(s) == 0

# 3. Функція перегляду верхнього елемента
def peek(s):
    if not is_empty(s):
        return s[-1]
    return "Стек порожній"

# 4. Реверс рядка за допомогою стеку
user_input = "Python"
temp_stack = []
for char in user_input:
    temp_stack.append(char)

reversed_string = ""
while not is_empty(temp_stack):
    reversed_string += temp_stack.pop() 

print(f"Реверс рядка '{user_input}': {reversed_string}")