import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi


# Визначаємо функцію
def f(x):
    return x ** 2

# Межі інтегрування
a, b = 0, 2
N = 10000




def monte_carlo_integral(f, a, b, N=10000):
    """
    Обчислення визначеного інтегралу методом Монте-Карло.
    
    :param f: функція, яку інтегруємо
    :param a: нижня межа інтегрування
    :param b: верхня межа інтегрування
    :param N: кількість випадкових точок
    :return: значення інтегралу
    """

    x_random = np.random.uniform(a, b, N)
    y_random = np.random.uniform(0, f(b), N)

    M = np.sum(y_random <= f(x_random))

    A_rectangle = (b - a) * f(b)
    
    return (M / N) * A_rectangle

# Обчислення інтегралу
integral_mc = monte_carlo_integral(f, a, b, N)
integral_quad, _ = spi.quad(f, a, b)

# Візуалізація
x_values = np.linspace(-0.5, 2.5, 400)
y_values = f(x_values)

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, 'r', linewidth=2, label='f(x) = x^2')
plt.fill_between(x_values, y_values, color='gray', alpha=0.3, label='Інтеграл (аналітично)')

x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)
plt.scatter(x_random, y_random, s=1, color='blue', alpha=0.2, label='Випадкові точки')

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
