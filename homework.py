# -*- coding: utf-8 -*import

import os

os.system('cls' if os.name == 'nt' else 'clear')

'''

Задача 34:  
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, 
насколько легко он их придумывает, Вам стоит написать программу. 
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
Фразы отделяются друг от друга пробелами. 
Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

Пример:

Ввод: пара-ра-рам рам-пам-папам па-ра-па-да    
Вывод: Парам пам-пам  

'''
# beat = input("Hello! Enter poem by Winnie the Pooh: ")

# def check_rhythm(beat):
#     lines = beat.split(" ")
#     syllables = []
#     for line in lines:
#         words = line.split("-")
#         syllables.append(sum([count_vowels(word) for word in words]))
#     if len(set(syllables)) == 1:
#         return "Пам парам"
#     else:
#         return "Парам пам-пам"

# def count_vowels(word):
#     vowel_letter = "оёеэюуыиая"
#     count = 0
    
#     for char in word:
#         if char.lower() in vowel_letter:
#             count += 1
    
#     return count

# result = check_rhythm(beat)

# print(result)

'''
Задача 36:

Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

Пример:

Ввод: `print_operation_table(lambda x, y: x * y) ` 
Вывод:

1 2 3 4 5 6

2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36

'''

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in a:
#         print(*[f"{x:>3}" for x in i])

# print_operation_table(lambda x, y: x * y)

'''
Задача 30:  
Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

'''
 
# a1 = int(input(" Hello! Please enter first element array: ")) 
# d  = int(input(" Great! Enter the difference of the array elements: ")) 
# n  = int(input(" Alright! Enter the number of array elements: "))

# for i in range(n): print (a1 + i * d)

'''
Задача 32: 

Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)

'''

# arr_1 = [-3, 9, 21, 32, 0, -145, 21, -44, 22, 43, 7]
# arr_2 = []
# max = 0
# min = -1
# for i in range(len(arr_1)):
#     if arr_1[i] >= min and arr_1[i] <= max:
#         arr_2.append(i)
# print(arr_2)

'''
Задача 22: 

Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
1. Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
2. Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
3. Пользователь вводит сами элементы множеств.
'''
# from random import randint
# n_set = set(randint(0, 100) for i in range(int(input(' Please, enter the number of elements of the first set: '))))
# print(n_set)
# m_set = set(randint(0, 100) for i in range(int(input(' Please, enter the number of elements of the second set: '))))
# print(m_set)
# s_set = sorted(n_set.intersection(m_set))
# print(*s_set)

'''
Задача 24: 

В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
'''
# from random import randint
# list_1 = list (randint(1, 5) for i in range(int(input(' Please, enter the number of bushes: '))))
# print(list_1)
# a = int(input(' Please, enter the number of the bush: '))
# res = 0
# if a == 1:
#     res = list_1 [0] + list_1[1] + list_1[-1]
# elif a == len(list_1):
#     res = list_1[-2] + list_1[-1] + list_1[0]
# else:
#     res = list_1[a-1] + list_1[a-2] + list_1[a]
# print(res, ' Berries ')

'''
Задача 10: 

На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
1. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороно. 
2. Выведите минимальное количество монет, которые нужно перевернуть.

5 -> 10110
2

'''
# coins = int(input('Hello! Please, enter the number of coins: '))
# obverse = 0
# reverse = 0
# for i in range(coins):
#     x = int(input('Please enter, if the coin is upside obvers - 1, and if reverse - 0: '))
#     if x == 1:
#         obverse += 1
#     else:
#         reverse += 1
#     if x > 1 or x < 0:
#         import sys
#         sys.exit("Error. Please try again")

# if obverse < reverse:
#     print(f'Flip {obverse} coin from obverse to reverse')
# elif obverse == reverse:
#     print(f'Flip all the coins with the obverse or all the reverse')
# else:
#     print((f'Flip {reverse} coin from reverse to obverse'))

'''
Задача 12:
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y ≤ 1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки:
1. Он называет сумму этих чисел S 
2. Их произведение P. 

Помогите Кате отгадать задуманные Петей числа.

4 4 -> 2 2
5 6 -> 2 3

'''

# s = int(input('Hello! Please, enter number S: '))
# p = int(input('Enter number P: '))

# x = (s-int((s**2-4*p)**0.5))//2
# y = (s+int((s**2-4*p)**0.5))//2
# print(x, y)

'''
Задача 14: 

Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
10 -> 1 2 4 8

'''
# n = int(input('Hello! Please, enter number N: '))
# m = 1
# while m <= n:
#     print(m, end = ' ')
#     m = m * 2