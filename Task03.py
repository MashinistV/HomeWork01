"""
Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.
"""
n = int(input("Введите шестизначное число: "))
while n > 999999 or n < 100000:
    print("Вы ввели не шестизначное число")
    n = int(input("Введите шестизначное число: "))
else:
    if (n % 10 + (n // 10) % 10 + (n // 100) % 10) == ((n // 1000) % 10 + (n // 10000) % 10 + (n // 100000) % 10):
        print("Это счастливый билет")
    else:
        print("Это несчастливый билет")