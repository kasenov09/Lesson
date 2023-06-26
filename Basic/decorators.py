''' Декораторы '''


# def outer(x):
#     def inner(y):
#         return x + y
#     return inner

# inner_func = outer(7)
# print(inner_func(3))


'''
Функция высшего порядка -> эта функция , которая может принимать в качестве аргумента другую функцию и/или возвращать функцию как результат
'''

# def test_func(func):
#     def inner_test_func():
#         func()
#         # <тело>
#     return inner_test_func


# def hello(func):
#     # <тело>
#     pass

'''
Декоратор -> функция высшего порядка (в качестве аргумента принимает функцию и возвращает функцию), которая оборачивает другую функцию для расширения ее функционала, при этом не изменяя ее код
'''

# def test_decor(func):
#     func()
#     print('hello')

# def a():
#     print('hi')

# test_decor(a)

# from typing import Callable
# def benchmark(func: Callable):
#     import time
#     start = time.time()
#     func()
#     end = time.time()
#     print(f'Время работы функции {func.name},заняло {end - start}')

# def loop():
#     i = 0
#     while i < 10000:
#         print(i)
#         i += 1

# benchmark(loop)

# def test_loop():
#     for i in range(1000000):
#         print(i)

# benchmark(test_loop)

'''Синтаксис'''
# def decorator(func):
#     def wrapper():
#         print('Фукция-обертка!')
#         print(f'Оборачиваем функцию {func.name}')
#         func()
#         print('Выходим из обертки')
#     return wrapper

# @decorator
# def say_hi():
#     print('hiiiiiiiiiiiiiiiii')

# say_hi()

# как работает @ под капотом
'''

@ -> синтаксический сахар , позволяет нам явно указать какой декаратор применяется для функции
под капотом вызывает функцию decorator и результат выполнения этой функции сохраняет в переменной с точно таким же названием как и обернутая функция
# say_hi = decorator(say_hi)
# say_hi()
'''
# def uppercase_decorator(func):
#     def wrapper():
#         func_ = func()
#         upper_str = func_.upper()
#         return upper_str
#     return wrapper


# @uppercase_decorator
# def inp_str():
#     str_ = input('Введите текст: ')
#     return str_


# print(inp_str())


# при использовании *args, **kwargs декаоратор будет универсальным
# def benchmark(func):
#     def wrapper(*args, **kwargs):
#         import time
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(f'Время работы функции {func.name},заняло {end - start}')
#     return wrapper

# @benchmark
# def loop(a, b, c, d):
#     i = 0
#     while i < 10000:
#         print(i)
#         i += 1

# loop(3, 4, c=9, d=8)


# def smart(func):
#     def wrapper(x, y):
#         print('============')
#         if y == 0:
#             return 
#         return func(x, y)
#     return wrapper

# @smart
# def division(x, y):
#     return x / y

# print(division(9, 0))
# print(division(9, 3))


# def decor(num):
#     def inner_decor(func):
#         def wrapper(*args, **kwargs):
#             for i in range(num):
#                 func(*args, **kwargs)
#         return wrapper
#     return inner_decor

# @decor(4) 
# def test(a, b):
#     print(f'============={a}\n+++++++++++++++++{b}')

# test(3, 4)



# def strong(func):
#     def wrapper():
#         return '<strong>' + func() + '</strong>'
#     return wrapper

# def div(func):
#     def wrapper():
#         return '<div>' + func() +' Зима близко' + '</div>'   
#     return wrapper


# # @strong
# # @div
# def get():
#     return 'hello makers'
# print(get())

# print(get())
# def call_multiple_times(n):
#     def decorator(func):
#         def wrapper(x, **y):
#             for _ in range(n):
#                 result = func(x, **y)
#             return result
#         return wrapper
#     return decorator


# @call_multiple_times(10)
# def greet(name):
#     print(f"Hello, {name}!")

# greet("John")












# def call_function(func): 
#     import calendar from

    # def wrapper() :
    #     print(f"Вызываю функцию {func.__name__}") 
    # func() 
    # print(f"Вызов функции {func.__name__} прошёл успешно") 
    # @call_function
    # def first(): 
    #     print("hello world") 
    #     return 'hello world' 
    # first()
    # return wrapper 



# Вывод:
# Вызываю функцию first
# hello world
# Вызов функции first прошёл успешно


# def func_start_time(func):  
#     import datetime 
#     def fune():
        
#         print('Функция запущена', datetime.datetime.now())
#         func()
#     return fune

# def func():
#     print('Hello World')
# c = func_start_time(func)
# c()
# def decorator(func):
#     def wrapper():
#         print('</b> декоратор make_bold <b>')
#         print(f' <i>декоратор make_italic</i>')
#         print('<u>декоратор make_underline</u>')
#     return wrapper

# @decorator
# def say_hi():
#     print('hiiiiiiiiiiiiiiiii')

# say_hi()





 

# def make_bold(func):
#     def make_bol():     
#                 return'<b>'+func()+ '</b>'
#     return make_bol
# def make_italic(func):
#     def make_itali():     
#         return '<i>'+func()+ '</i>'
#     return make_itali
# def make_underline(func):
#     def make_underlin():    
#         return '<u>' +func()+ '</u>'
#     return make_underlin
# @make_bold
# @make_italic   

# @make_underline 

# def hello():
#     return 'Hello world'
# print(hello())




# def strong(func):
#     def wrapper():
#         return '<strong>'
#     return wrapper

# def div(func):
#     def wrapper():
#         return '<div>'  
#     return wrapper




# def get():
#     return 'hello makers'
# print(get())

# def benchmark(func):
#     def fetch_webpage():
#         import time
        
#         start = time.time()
#         func()
#         time.get('https://google.com')
#         end = time.time()
#         print(f'Время работы функции {func.name},заняло {end - start}')
#     return fetch_webpage
    
# print(benchmark)
