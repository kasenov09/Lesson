# '''логичкские выражение и оператторы'''
# '''Boolean'''
# # неизменяемые тип данных
# # true/false
# # print(bool(00000)) #false
# # print(bool(3)) #true
# # print(bool(False)) #false
# # print(bool('false')) #true
# # print(bool(' ')) #true
# # print(bool(''))
# # print(bool(-234))


# '''логичекские выражение  ->  выражение, которые возврощает Boolean Type'''


# #  === -> сравнение
# 5 == 5 #true
# 4 == 6 #false
# '5' == 5 #false

# # != ->не равно
# 5 != 5 #false
# 6 != 4 # true

# # >(больше)
# 5 > 2  #true
# 6 > 9 #false
# 5 > 5 #false

# # < (меньше)
# 3 < 4 #true
# 3 < 1 #false
# 3 < 3 #false


# # >= -> больше или равно
# 6 >= 5 #true
# 6 >= 6 #true
# 6 >= 9 #false


# #<= -> меньше или равно
# 4 <= 3 #false
# 4 <=5 #true
# 4 <= 4 #true



# '''and or not'''
# # and -> логическое и
# # or -> лагическое или
# # not -> логическое отрицание

# #and  используется для объедениние
# # or    логическое выражение

# a = 5
# b = 6

# # #true     #true
# # a ==5 and b == 6 #true
# # a ==4 and b == 6 # false

# # если все части выражения возвращает true, то все выражение возврашает true
# # если хотябы одна часть выражение
# # возвращает False -> False

# a ==5 or b == 6 #True
# a ==4 or b == 6 #true
# a ==4 or b == 9 #false
# # если хотя бы она часть выражение возвращает true
# #то все выражение возврощает тоже True

# # not

# # print(not True) #false
# # print(not False) #true
# not a == 5 # false
# not b == 6 #true

# '''щператоры идентификации'''
# # 1. in -> прверяет наличие элемента
# # 2. сравнение
# #  == -> по значению 
# # is -> по ячейке памяти
# # 3. is not -> отрицательное сравнение ячеек памяти



# '''========== None Type==========='''
# # не изменяемые тип данныых с одним значением None
# #Используется для обозначение пустых значений

# bool(None)# False\
# bool('None')#true

# # a - None
# # print(a == None)



# '''=======условные операторы======'''
# #нужны для того чтобы при разных входных данных код выполняется по разному


# if условие: 
#     тело
# # тело будет работать если условия True(веррно)

# if условие1:
#     тело1
# else:
#     тело2
# #тело1 будет работать если условие один верно
# #тело2 будет работать еслит условия1 не верно (во всех случаях)


# if условие1:
#     тело1
# elif:
#     тело3
# else:
#     тело2

number = int(input('number'))
if number > 0:
    print('ok')
elif number < 0 :
    print('no')
else:
    print('not')


'''Тернантные условие'''
#условие в одну строку if else

# Cинтаксис
# тело1 if условие else тело2

# num = 9
# result = 'hello' if num == 9 else 'World'
# print(result)

'''========= Маржове операторы==========='''
# позволяет нам ка присваивать значение так возврощать его в одном выражение

# print(hello :='hello') #true
# print(hello = 'hell#error

# number = int(input('number'))
# if number % 2 == 0:
#     print('четный')
# else:
#     print('не четный')
#    




