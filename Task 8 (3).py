def counting_month(money_capital, spend, month=0):
    """Определяем сколько месяцев можно прожить
    на финансовую подушку и зарплату"""
    while True:
        money_capital += salary
        spend = spend + (spend * increase)
        money_capital -= spend
        month += 1
        if money_capital < spend:
            print(month)
            break


money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
counting_month(money_capital, spend)
