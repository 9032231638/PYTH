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

# N = int(input('Введите кол-во элементов массива А: '))
# Ai = input("Введите через пробел эл-ты массива А: ").split()
# An = list(map(int, Ai))
# X = int(input('Введите искомое число X: '))
# min = (X - An[0])
# i = 0
# for i in range(1, N):
#     c = (X - An[i])
# print(f'Число {An[i]} в массиве A наиболее близко по величине к числу {X}')

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

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# from random import randint
# n_set = set(randint(1, 20) for i in range(int(input("Введите кол-во элементов первого множества: "))))
# print(n_set)
# m_set = set(randint(1, 20) for i in range(int(input("Введите кол-во элементов второго множества: "))))
# print(m_set)
# s_set = sorted(n_set.intersection(m_set))
# print(*s_set)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# n = int(input("Введите кол-во  кустов: "))
# arr = list()
# for i in range(n):
#     x = int(input("Введите кол-во ягод: "))
#     arr.append(x)
#     arr_count=list()
# for i in range(len(arr)-1):
#     arr_count.append(arr[i-1]+arr[i]+arr[i+1])
# arr_count.append(arr[-2]+arr[-1]+arr[0])
# print(arr)
# print("Максимальное число ягод за один заход ", max(arr_count))

# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# def Number(A,B):
#      if B == 0:
#         return 1
#      return A**B       
# A=int(input("Введите число A: "))
# B=int(input("Введите число B: "))
# print(Number(A,B))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# def sum(a,b):
#     if b==0:
#         return a
#     return 1+sum(a,b-1)
# a=int(input("Введите число a: "))
# b=int(input("Введите число b: "))
# print(sum(a,b))

# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a1=int(input("Введите значение 1-го элемента: "))
# d=int(input("Введите разность элементов: "))
# n=int(input("Введите количество элементов: "))
# res = [a1 + (i - 1) * d for i in range(1, n + 1)]
# print(*res)

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# list=[-5,9,0,3,-1,-2,1,4,-2,10,2,0,-9,8,10,-9,0,-5,-5,7]
# min_number = int(input("Введите min диапазон "))
# max_number = int(input("Введите max диапазон "))
# for i in range(len(list)):
#     if min_number <= list[i] <= max_number:
#         print(i)

# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# def poems(str):
#     str = str.split()
#     list_1 = []
#     for word in str:
#         sum = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 sum += 1
#         list_1.append(sum)
#     return len(list_1) == list_1.count(list_1[0])

# text = input("Введите фразу: ")
# if poems(text):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# def print_operation_table(operation, num_rows, num_сolumns):
#     arr=[[operation(i,j) for i in range(1,num_rows+1)] for j in range(1, num_сolumns+1)]
#     for i in arr:
#         print(*[f"{x:>3}"for x in i])
# line = int(input("Введите кол-во строк: "))
# columns = int(input("Введите кол-во столбцов: "))
# print_operation_table(lambda x,y: x*y,columns,line)
