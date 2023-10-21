money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
zp=salary+money_capital
count=0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
for i in range (0,10):
    if zp>0:
        zp=zp-spend
        spend=spend+spend*increase*i
        zp=zp+5000
        count+=1

print("Количество месяцев, которое можно протянуть без долгов:", count)
