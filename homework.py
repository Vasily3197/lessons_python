# -*- coding: utf-8 -*import

import os

os.system('cls' if os.name == 'nt' else 'clear')

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