'''==========Строки ============'''
#  неизменяемые типы данных, которые предназначены для хронения последовательности символов, заключенной в одинарной или двойные кавычки


# string = "Строка"
# string2 = 'Строка'
# # string3 = 'неправельно"
# string4 = "don't"
# string5 = 'he: "hello"'
string6 = '''
hello
dc
ds
'''
string7 = """
hello
dsd
dds
"""

# print(string6)

'''Экранированные последотельности'''
# Последовательнсть символов, начинающаяся
# с ->
'\n' # перенос строки
'\t' # табуляция (4 пробела)
'\\' # для отоброжение \
'\"' # для отоброжение "
'\'' # для отоброжение '
'\r' # возвращает каретку в начало строки
'\v' # вертикальная табуляция



# string = 'sidhfrkuahguieм\vlhluieahufeahheajbvhas\vfosvjaif'
# print(string)

'''конкатенация  склеивание строк'''
# str = 'Hello '
# str_1 = 'Lolol'
# print(str + str_1)



'''Дублирование строк'''

# print (str, str_1) 
# print (str *3) 

'''========= форматирование строк ========='''
# 1. С использованием %
# 2. C использованием метода .format()
# 3. интерполяция строк (f строки)

# name = input('enter your name:')
# a = input()
# result = 'Hellotima, %s' %name 
# print(result, name)

# .format()
# name = input('Enter your name:')
# age= input('Enter your age:')
# test= input('Enter your age:')
# result = 'Hello, {} {} {}' .format(name,age,test)
# print(result)


# f- строки
# name = input('Enter your name:')
# age= input('Enter your age:')
# test= input('Enter your age:')
# result = f'Hello {name} your are {age}2вyears old  {test} '
# print(result)


'''=========Индексы=========='''
# Порядковый номер символов в строке
' Hello world'
# 012345678910
# 
# str_ = 'hello'
# # print(str_[0])
# str_[1]# полученние первого элемента строки
# str_[-1] #полученние последнего элемента строки


'''========= Cзрезы ==========='''
# получение подстроки (какой то части строки)
# Синтаксис [начало : конец: шаг]
# print(str_[:5])
# print(str_[6:])
# print(str_[-2::-1])


'''============ методы строк ============='''
# метод - та же самая функция, но обращаемся к ней через точку

# print(dir('hello'))

# методы на is -> проверяют
# возвращают True/False
# str.isalnum() -> состоит ли строка только из букв и/или чисел
# str.isalpha() -> состоит ли строка только из букв
# str.isdigit() #->  состоит ли строка толлько из чисел
# str.islower() #-> находится ли строка в нижнем регистре
# str.isupper() # -> состоит ли строка из символов верхнего регистра
# str.isspace() # -> состоит ли строка из неотображаемых символов (пробелы и экранированные последовательности)
# str.isnumeric() # ->  состоит ли строка толлько из чисел

# print('hello9'.isalpha())
# print('1234 '.isdigit())


# str.upper() -> переводит в верхний регистр
# str.lower() -> переводит в нижний регистр

# str_ = 'Makers'
# a = str_.lower() #makers
# print(a)

# str_ = 'Makers'
# a = str_.upper() #MAKERS
# print(a)

# str.title() -> каждое слово в строке запишет с заглавной буквы

# str.capitalize() -> только самое первое слово в строке запишет с заглавной 

# str_ = 'hello Makers'
# print(str_.title()) # Hello Makers
# print(str_.capitalize()) #Hello makers

# strip() -> убирает пробелы в начале и в конце строки (rstrip, lstrip)
# len() -> возвращает длину строки
# 
# a = input('here: ')
# b = a.strip()
# print(len(a), a, len(b), b)


# str.replace(old, new, count) -> заменяет old значение в строке на new, count - отвечает за кол-во замен

# str_ = 'ha ha ha a'
# new_str = str_.replace('ha', 'new', 1)
# print(new_str)

# str.split('разделитель') -> делит строку по разделителю и возвращает список. разделитель по умолчанию -> пробел

# a = 'hello makers boot incubator test'
# b = a.split('t')
# print(b)
# string = 'Hello'
# print(f" \n {string}"*3)
numbers = input() 
sum = sum(map(int, numbers.split(' ')))
print(sum)
