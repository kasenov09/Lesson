'''Области видимости и пространства имен'''

''' Пространство имен'''

'''
1. builtins (встроенное) -> все что встроено в стандартную библиотеку питона
print
input
len
'''
'''
2. Global -> (глобальное) все переменные внутри файла , которые мы создали (без табуляции)
'''

# name = 'Sam'


'''
3. Enclosed -> (не локальное, замкнутое) находится между двумя пространствами

'''

'''
4. local -> (локальное) 
# '''
# def test():
#     hello = 'hello'

# print(globals()) -> возвращает все глобальные переменные

# print(dir(builtins)) -> возвращает все встроенные имена


# x = 100
# y = 0
# z = 99
# globals()['x'] = 45
# print(z is globals()['z'])
# print(globals())


'''
Локальные переменные (в функциях)
'''
# locals()-> возвращает имена локального пространства,возвращает все локальные имена
# def func(test):
#     a = 10
#     b = 0
#     print(locals())

# func(6)

# print(locals()) -> когда применяем на глобальном уровне , возвращает все глобальные имена

# def func():
#     a = 0
#     b = 9
#     print(a, b)

# func()


'''Enclosed'''

# возникает тогда , когда внутри функции объявляется еще функция (при вложенности функций)

# def outer_func():
#     outer = 10 -> 'enclosed'
#     print(outer)
#     def inner_func():
#         inner = 11 -> 'local'
#         print(inner)
#     inner_func()
#     print(locals())

# outer_func()

# string = 'я глобальная'
# def outer_func():
#     string = 10 
#     print(string)
#     def inner_func():
#         string = 11 
#         print(string)
#     inner_func()
#     print(locals())

# outer_func()
# # inner_func() -> будет ошибка , так как она в нелокальной области
# print(outer_func())


''' Порядок поиска переменных '''
# Local -> Enclosed -> Globak -> Builtins


# import this # краткий гайд по Дзен Питону

''' global -> плзволяет изменить значение глобальной переменной , находясь в локальной области видимости'''
# x = 10

# def func():
#     global x
#     x = 20
#     print(x)

# func()
# print(x)

# x = [1, 2, 3]

# def func():
#     global x
#     x = [3, 4, 5]
#     x[0] = 0
#     print(x)

# func()
# print(x)


# count = 0

# def couter():
#     global count
#     count += 1
#     print(count)

# couter()
# couter()
# couter()

# a = 0
# def outer():
#     global a
#     a = 8
#     def inner():
#         global a
#         a = 10
#         print('inner a = ', a)
#     inner()
#     print('outer a = ', a)

# outer()
# print('global a = ', a)

''' 
nonlocal -> позволяет изменить значение enclosed переменной в локальной области видимости
'''


# a = 0
# def outer():
#     a = 8
#     def inner():
#         nonlocal a
#         a = 10
#         print('inner a = ', a)
#     inner()
#     print('outer a = ', a)

# outer()

# from time import sleep

# def counter(number):
#     count = 0

#     def add():
#         nonlocal count
#         count += 1
#         print(count)
#         sleep(1)

#     for i in range(number):
#         add()

# counter(10)





# x ='Я глобальная переменная!'
# def my_func():
#     global x
#     x = 'Я могу изменяться'
#     print(x)
    
# my_func()



# Дана глобальная переменная num со значением 3. Напишите функцию mul которая будет возвращать квадрат этой переменной и записывать результат в глобальную переменную num. Вызовите функцию три раза, и распечатайте переменную num.

# mul()
# mul()
# mul()
# print(num)

# Output:

# 6561

# тaк кaк num перезаписали на 9(3*3 = 9) затем на 81

# (99 = 81) и после на 6561(8181 = 6561)
# num = 3*3
# def mul():
#     global num
#     num = (((num)*num)*num)*num
#     print(num)
# mul()




# В Python есть встроенная арифметическая функция pow(), pow принимает два обязательных аргумента x, y и один необязательный z и возвращает результат в виде x**y % z - возводит первое число в степень y и если передано третье число, делит результат на третье число и возвращает остаток.

# Пример использования pow:

# print(pow(2,3))
# # 8 - тaк кaк 2**3 = 8

# print(pow(2, 3, 3))
# # 2 - т.к 2**3 = 8, а остаток от деления 8 % 3 = 2

# У вас есть глобальная переменная result = 0. Напишите функции pow_first(x,y), отвечает за первую часть встроенной функции pow и pow_second(z), отвечает за вторую часть pow(z). Вызовите эти функции, а затем выведите переменную result.

# Пример:

# pow_first(2, 3)
# pow_second(3)
# print(result)

# Output:

# 2
# result = 0

# def pow_first(x, y):
#     global result
#     result = x ** y

# def pow_second(z):
#     global result
#     result = result % z

# pow_first(2, 3)
# pow_second(3)

# print(result)

# var = 'переменная в foo' 
# def foo(): 
#     global var
#     var = 'переменная foo' 
#     print('переменная в foo: ', var) 
#     def bar(): 
#         global var 
#         var = 'переменная bar' 
#     bar() 
# foo() 
# print('переменная в foo: ', var)

# a = ['pipi', 'papa', 'mama']
# b = [a]
# b.title(a)
# print(a)

a = [a for a in range(11)]
print(a)