# # Задача 2: Найдите сумму цифр трехзначного числа.

# print ("Введите трехзначное число:")
# num = int(input())
# sum = 0
# while num > 0:
#     x = num % 10
#     sum += x
#     num //= 10
# print(f"Сумма цифр трехзначного числа = {sum}")

# # Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# # Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# # количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# # Петя = x журавликов
# # Серёжа = y журавликов = Петя
# # Катя = z = (x+y)*2 журавликов
# # s = x + y + z = x + x + (x + x) * 2 = 6x журавликов
# # x = s / 6 журавликов

# print ("Введите количество журавликов:")
# s = int(input())
# x = s//6
# y = x
# z = (x+y)*2
# print(f"Петя сделал {x} журавликов")
# print(f"Катя сделала {z} журавликов")
# print(f"Сережа сделал {y} журавликов")

# # Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# # Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# # Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# print("Введите номер билета, 6 цифр:")
# ticket = int(input())
# firsthalf = ticket//1000
# sum1 = 0
# while firsthalf > 0:
#     i = firsthalf % 10
#     sum1 += i
#     firsthalf //= 10
# secondhalf = ticket % 1000
# sum2 = 0
# while secondhalf > 0:
#     j = secondhalf % 10
#     sum2 += j
#     secondhalf //= 10
# if sum1 == sum2:
#     print("Вы нашли счастливый билет")
# else:
#     print("Ваш билет не является счастливым")

# # Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# # если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# print("Введите длину n:")
# n = int(input())
# print("Введите ширину m:")
# m = int(input())
# print("Введите количество долек:")
# k = int(input())
# if k%m == 0 or k%n == 0:
#     print("Шоколадку можно разделить пополам")
# else:
#     print("Шоколадку нельзя разделить пополам")