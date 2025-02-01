import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначаємо функцію
def f(x):
    return x ** 2

# Межі інтегрування
a, b = 0, 2

# Кількість випадкових точок
N = 10000

# Генеруємо випадкові точки
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

# Підрахунок точок під кривою
M = np.sum(y_random <= f(x_random))

# Площа прямокутника
A_rectangle = (b - a) * f(b)

# Обчислення інтегралу методом Монте-Карло
integral_mc = (M / N) * A_rectangle

# Аналітичне обчислення інтегралу
integral_quad, _ = spi.quad(f, a, b)

# Візуалізація
x_values = np.linspace(-0.5, 2.5, 400)
y_values = f(x_values)

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, 'r', linewidth=2, label='f(x) = x^2')
plt.fill_between(x_values, y_values, color='gray', alpha=0.3, label='Інтеграл (аналітично)')
plt.scatter(x_random, y_random, s=2, color='blue', alpha=0.2, label='Випадкові точки')

# Додаємо вертикальні лінії для меж інтегрування
plt.axvline(x=a, color='gray', linestyle='--')
plt.axvline(x=b, color='gray', linestyle='--')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Графік інтегрування f(x) = x^2 від 0 до 2')
plt.legend()
plt.grid()
plt.show()

# Виведення результатів
print(f'Метод Монте-Карло: {integral_mc}')
print(f'Аналітичне значення (quad): {integral_quad}')
print(f'Різниця: {abs(integral_mc - integral_quad)}')
