#Задача 2: Найдите сумму цифр трехзначного числа.
n = int(input("Введите трехзначное число: "))
while n > 999 or n < 100:
    print("Вы ввели не трехзначное число")
    n = int(input("Введите трехзначное число: "))
else:
    print("Сумма цифр числа:", n % 10 + (n // 10) % 10 + (n // 100) % 10)