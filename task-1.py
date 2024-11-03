import pulp

if __name__ == "__main__":
    model = pulp.LpProblem("Максимізація_Виробництва", pulp.LpMaximize)

    lemonade = pulp.LpVariable("Лимонад", lowBound=0, cat='Integer')
    fruit_juice = pulp.LpVariable("Фруктовий_сік", lowBound=0, cat='Integer')

    model += lemonade + fruit_juice, "Загальне_виробництво"

    model += 2 * lemonade + 1 * fruit_juice <= 100  # Обмеження_води
    model += 1 * lemonade <= 50  # Обмеження_цукру
    model += 1 * lemonade <= 30  # Обмеження_лимонного_соку
    model += 2 * fruit_juice <= 40  # Обмеження_фруктового_пюре

    model.solve()

    # Виведення результатів
    print(f"Статус: {pulp.LpStatus[model.status]}")
    print(f"Вироблено Лимонаду: {lemonade.varValue}")
    print(f"Вироблено Фруктового соку: {fruit_juice.varValue}")
    print(f"Загальне виробництво: {lemonade.varValue + fruit_juice.varValue}")
