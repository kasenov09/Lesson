# Виды коментариев 
'''
1. Многострочный 
'''
"""Многострочный"""
# 2.

'''
Обзор типов данных
Типы данных в Питонне
'''

# 1. NoneType -> None 
# 2. Boolean (bool)-> True/False
# 3. Числовые типы данных:
    # a. integer (int()) -> 1 2 3 ... Целые числа 
    # b. float () -> 1.6  5.99 Числа с плавающей точкой
    # c. complex(3, 5) -> 3 + 5j Комплесные числа 
# 4. string (str()) -> "hello" 'makers """ """ ''' ''' ... Строки
# 5. list() -> [1, 2, 3, None, True, 'Hello', [1, 2, 3], {1: 'a'}] Списки
# 6. tuple() -> (1, 2, 3, None, False) Кортеж
# 7. set() -> {1, 2, 3, 4, 5}
# 8. dict() -> {1: 'one', 2: 'two'} Словарь
# 9. frozenset() -> замороженное множество 

'''Изменяемые (Mutable)'''
# set()
# dict()
# list()


'''=========== Переменные ==========='''
# ссылка на ячайку памяти в которой хранится обьект. Предназначена для хранения

# hello_world = 'snake case'
# helloWorld = 'camel case'

# num = 10
# num_2 = 11
# name = 'John'
# age = 32 
# is_user = True 

# print() -> Функция для вывода данных в терминал

# print(hello_world)
# print(helloWorld)

# num3 = num + num_2
# print(num3)

# input() -> Функция ввода данных с терминала 

# name = input('Enter your name: ')
# print(name)

3
    # два разных обьекта 
'3'
# type() -> выводит тип данных
# print(type(3))
# print('3' + '3')

# int() -> для перевода в тип данных целые числа 

# number1 = int(input('Введите число: '))
# # print(int(number1))
# print(type(number1))

# a = 1
# b = 2

# # id() -> выводит номер ячейки  в памяти

# print(id(a), id(b))

# list_ =[1, 2, 3, 4,]
# print(list_)
# print(id(list_))
# list_.append(5)
# print(list_)
# print(id(list_))

'''===========операция над числами============'''

# % -> для получение остатка от деление
# number1_ = 88
# number2_ = 10
# print(number1_ % number2_)

# .. ->  целочисленное давление
# number1_ = 88
# number2_ = 10
# print(number1_ // number2_)

# # возведение стеени
# print(10**2)
# print(5**6)

# модуль числа -> |-9| из отрицательного числа сделать положительное
# print(abs(-9))
# print(abs(10))

# pow -> 1. возведение в степень
        #  возврашение остаток от деление первого результата
        #  )(возведения в степень) на третье число

# 1. 
# print(pow(5, 4))
# # 2.
# print(pow(5,3,9))


#  divmode() -> принимает два числа и возврощает два числа ->
# первое число - результат целочисленного деление, второе -> остаток от деление

# print(divmod(9, 4))
# divmod(15, 5) 

# round()
# print(round(559/5))
# print(round(559/5, 2))  второй элемент, указывает сколько чисел после запятой оставить

import math

# print(dir(math))

# from math import sqrt

# math.sqrt()

# sqrt  -> для нахождение квадратнаго корня
# print(math.sqrt(100))
# # math.sqrt(36)

# inp1=input()
# inp2=input() 
# inp3=input() 
# print((inp1*inp2)%inp3)




# year = int(input())
# if year%100 ==0:
#     print('NO')
# elif year%4 == 0:
#         print('YES')
# elif year%200 == 0:
#         print('YES')
# else:
#         print('NO')


#     Создайте список чисел nums и число target.
#     С помощью условных операторов выведите, есть ли число   в этом списке, если есть выведите в консоль Да, если нет выведите Нет.

# Например, если дан список [1, 15, 36, 88], а в переменной target хранится число 15, вывод будет:

nums = [1, 2, 3, 4, 5]
target = 88
if target in nums :
        print('есть')
else:
        print('нет')