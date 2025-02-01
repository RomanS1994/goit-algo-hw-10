from pulp import *

# Оголошуємо задачу лінійного програмування
model = LpProblem(name="maximize_production", sense=LpMaximize)

# Змінні (кількість виробленого лимонаду та фруктового соку)
lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

# Цільова функція (максимізація загальної кількості продуктів)
model += lemonade + fruit_juice, "Total Production"

# Обмеження ресурсів
model += (2 * lemonade + fruit_juice <= 100), "Water Constraint"
model += (lemonade <= 50), "Sugar Constraint"
model += (lemonade <= 30), "Lemon Juice Constraint"
model += (2 * fruit_juice <= 40), "Fruit Puree Constraint"

# Розв'язуємо задачу
model.solve()

# Виводимо результати
print(f"Оптимальна кількість лимонаду: {value(lemonade)}")
print(f"Оптимальна кількість фруктового соку: {value(fruit_juice)}")
print(f"Максимальна загальна кількість напоїв: {value(model.objective)}")