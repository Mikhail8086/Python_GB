hours = 0
minutes = 0
seconds = 0

seconds = int(input("Введите время в секундах: "))

if seconds >= 3600:
    hours = seconds // 3600
    seconds %= 3600

if seconds >= 60:
    minutes = seconds // 60
    seconds %= 60

print(f"Время в формате: чч:мм:сс - {hours}:{minutes}:{seconds}")

