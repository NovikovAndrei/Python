def counting_money(salary, spend, months, increase, need_money=0):
    """Определяем какую сумму надо иметь, чтобы
    прожить определенное количество месяцев"""
    for i in range(months):
        if i > 0:
            spend *= 1 + increase
        need_money += spend - salary
    print(round(need_money))


salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

counting_money(salary, spend, months, increase)
