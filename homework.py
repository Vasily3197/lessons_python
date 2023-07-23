# -*- coding: utf-8 -*import

import os

os.system('cls' if os.name == 'nt' else 'clear')

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