# print(5, 9, 4)

# Задача 2: Найдите сумму цифр трехзначного числа.

# d = int(input("Введите трехзначное число: "))
# print(d // 100 + (d // 10) % 10 + d % 10)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
#           Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
#           что Петя и Сережа сделали одинаковое количество журавликов,
#           а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# s = int(input("Введите общее кол-во сделанных журвликов"))
# print("Катя сделала ", s//6*4, "шт")
# print("Петя сделал ", s//6, "шт")
# print("Сережа сделал ", s//6, "шт")

# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# n = input("Введите номер билета")
# s1 = int(n[0]) + int(n[1]) + int(n[2])
# s2 = int(n[3]) + int(n[4]) + int(n[5])
# if s1 == s2:
#     print('yes')
# else:
#     print("no")

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# a = int(input("Введите кол-во долек 1-ой стороны "))
# b = int(input("Введите кол-во долек 2-ой стороны "))
# c = int(input("Введите желаемое кол-во долек "))
# if c < a * b and c % a == 0 or c % b == 0:
#     print("yes")
# else:
#     print("no")

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input("Введите кол-во монет "))
# a = 0
# b = 0
# for i in range(n):
#     x = int(input("Введите сторону монеты, где герб=1, решка=0, по очереди "))
#     if x == 0:
#         a += 1
#     else:
#         b += 1
# if b > a:
#     print(a)
# else:
#     print(b)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# x = (int(input('Введите число X ')))
# y = (int(input('Введите число Y ')))
# S = x + y
# P = x * y
# k = 0
# for i in range(1001):
#     if k != 1:
#         for j in range(1001):
#             if k != 1:
#                 if S == i + j and P == i * j:
#                     print(i, j)
#                     k = 1
#             else:
#                 j = 1001
#     else:
#         i = 1001

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input("Введите число "))
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1

# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
 
# n = int(input('Введите размер массива: '))
# list_n = input('Введите элементы массива через пробел: ').split()
# arr = list(map(int, list_n))
# x = int (input('Введите искомое число х: '))
# k = 0
# for i in range(n):
#     if arr[i] == x:
#         k += 1
# print(f'Число {x} встречается в массиве А {k} раз.')

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# N = int(input('Введите количество элементов массива А: '))
# Ai = input("Введите через пробел элементы массива А: ").split()
# An = list(map(int, Ai))
# X = int(input('Введите искомое число X: '))
# min = (X - An[0])
# i = 0
# for i in range(1, N):
#     c = (X - An[i])
# print(f'Число {An[i]} в списке A наиболее близко по величине к числу {X}')

# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# N = int(input('Введите 1, для англ.языка, или 0, для в рус.языка: '))
# eng_dic = {1:'AEIOULNSTR',2:'DG',3:'BCMP',4:'FHVWY',5:'K',8:'JZ',10:'QZ'}
# rus_dic = {1:'АВЕИНОРСТ',2:'ДКЛМПУ',3:'БГЁЬЯ',4:'ЙЫ',5:'ЖЗХЦЧ',8:'ШЭЮ',10:'ФЩЪ'}
# word = input('Введите слово: ').upper()
# if N == 1:
# 	print('Вы получаете', sum([k for i in word for k, v in eng_dic.items() if i in v]), 'очков')
# elif N == 0:
#     print('Вы получаете', sum([k for i in word for k, v in rus_dic.items() if i in v]), 'очков')

