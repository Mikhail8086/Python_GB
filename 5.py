revenue = 0
costs = 0
profit = 0

revenue = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))
profit = revenue - costs

if profit < 0:
    print("Финансовый результат фирмы:", profit, "р.", "- Убыток!")
if profit == 0:
    print("Финансовый результат фирмы:", profit, "р.", "Сработали в ноль!")
if profit > 0:
    print("Финансовый результат фирмы:", profit,"р.","- Прибыль!")