n = 0
n = int(input("Введите целое число: "))

ls = []
while n > 1:
    ls.append(n % 10)
    n = n // 10
r = max(ls)
print(r)
print (ls)
print(n)

