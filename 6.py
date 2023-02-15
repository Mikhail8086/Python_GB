revenue = 0
costs = 0
profit = 0
profitability = 0
employees = 0
profit_employees = 0

revenue = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))
profit = revenue - costs

if profit < 0:
    print("Финансовый результат фирмы:", profit, "р.", "- Убыток!")
if profit == 0:
    print("Финансовый результат фирмы:", profit, "р.", "Сработали в ноль!")
if profit > 0:
    print("Финансовый результат фирмы:", profit,"р.","- Прибыль!")
    profitability = (profit / revenue) * 100
    profitability = float('{:.2f}'.format(profitability))
    print ("Рентабельность фирмы:", profitability,"%")
    employees = int(input("Введите кол-во сотрудников: "))
    profit_employees = profit / employees
    profit_employees = float('{:.2f}'.format(profit_employees))
    print("Прибыль в расчете на одного сотрудника:", profit_employees,"р.")
