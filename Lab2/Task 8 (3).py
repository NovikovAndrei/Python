def counting_month(money_capital, spend, month=0):
    """Определяем сколько месяцев можно прожить
    на финансовую подушку и зарплату"""
    while money_capital >= spend:
        money_capital += salary - spend
        month += 1
        spend *= 1 + increase
        
    print(month)


money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
counting_month(money_capital, spend)
