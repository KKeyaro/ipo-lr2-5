n = int(input("Введите число состоящее из 8 разрядов:"))
d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10
d3 = n % 10
n = n // 10
d4 = n % 10
n = n // 10
d5 = n % 10
n = n // 10
d6 = n % 10
n = n // 10
d7 = n % 10
n = n // 10
print("Сумма цифр числа:", n + d1 + d2 + d3 + d4 + d5 + d6 + d7)
