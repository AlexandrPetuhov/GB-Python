# # Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# # Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# # В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# N = int(input("Введите количество эленментов массива: "))
# A = []
# count = 0
# for i in range(1, N+1):
#     A.append(i)
# print(A)
# x = int(input("Введите число: "))
# for i in range(len(A)):
#     if A[i] == x:
#         count+=1
# print(count)

# # Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# # Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# # В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# N = int(input("Введите количество эленментов массива: "))
# A = []
# count = 0
# for i in range(1, N+1):
#     A.append(i)
# print(A)
# x = int(input("Введите число: "))
# for i in range(len(A)):
#     if x > A[i] or x == A[i]:
#         count += 1
# print(count)

# # *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# # В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# # D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# # А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
# # Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# # Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# # Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# dictionary = {1: "AEIOULNSTRАВЕИНОРСТ", 2: "DGДКЛМПУ", 3: "BCMPБГЁЬЯ", 4: "FHVWYЙЫ", 5: "KЖЗХЦЧ", 8: "JXШЭЮ", 10: "QZФЩЪ"}

# word = (input("Введите слово: ")).upper()
# cost = 0
# for i in word:
#     for key, value in dictionary.items():
#         if i in value:
#             cost += key
# print(f'Слово "{word}" оценивается в {cost} очков')

# # Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# # Количество повторов добавляется к символам с помощью постфикса формата _n.

# # Input: a a a b c a a d c d d
# # Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# string = "a a a b c a a d c d d".split()
# print(string)
# dictionary = {}
# for i in string:
#     if i in dictionary:
#         print(f'{i}_{dictionary[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     dictionary[i] = dictionary.get(i, 0) + 1

# Задача №27.Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells that she sells are sea shells 
# I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
print(text)
text = text.lower()
print(text)
d = set(text)
print(d)
print(len(d))

