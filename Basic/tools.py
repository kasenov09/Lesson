'''Циклы'''
# повторяющийся блок кода

# for -> проходится по итерируемому объекту
# list -> [1, 2, 4]; str -> 'hello world'; set -> {'hello', 'test', 'makers' }; dict -> {1: 'a', 2: 'b'}; tuple -> (1, 4, 7, 8) 

# while -> работает пока условие верно

# while <логическое выражение>:
#     тело

'''Бесконечный цикл'''
# a = 0
# while True:
#     # a = a +1 
#     a += 1
#     print(f'hello {a}')

'''цикл, который никогда не заработает'''
# while False:
#     print('hello')


# a = 0
# while a < 10:
#     # a = a +1 
#     a += 1
#     print(f'hello {a}')

# a = 11
# while a > 0:
#     print(a)
#     a -= 1


# a = 0
# while a != 100:
#     a += 1
#     print(a)

# list_ = ' '
# print(bool(list_))

'''найти сумму цифер целого числа'''
# number = int(input('Enter number: '))
# 12345 -> 15
# 1 + 2 + 3 + 4 + 5 = 15

# sum_ = 0
# for i in str(number):
#     sum_ += int(i)

# print(sum_)

# sum_ = 0
# l = 0

# while l < len(str(number)):
#     # print(str(number)[l])
#     sum_ += int(str(number)[l])
#     l += 1
    

# print(sum_)

# '4134567432'
# '4' -> 4
# for i in 12345665432:
#     print(i)


'''бесконечный цикл for'''
# list_ = [1, 2]
# for i in list_:
#     list_.append(i)
#     print(i)

# string = 'hello'
# print(id(string))

# for i in string:
#     print(i)
#     string = string + 'hello' # меняется ссылка на объект
# print(id(string))



'''break, continue, pass, else'''
# a= 0
# while a!= 11:
#     a+=1
#     print(a)
#     if a == 5:
#        break

#break ->полностью  выйти из цикла , досрочное прерывание цикла
# continue -> прейти к седующей итерации
# (нчинает следующий переход цикла, минуя оставшееяся цикла)

# i = 0
# while i<6:
#     i += 1
#     if i ==3:
#         continue
#     print(i)

# a = [1, 2, 3, 4, 'hello', 9, False]

# sum_ = 0
# for i in a:
#     if type(i)not in (int, float):
#         continue
#     sum_ += i
# print(sum_)



# for i in range(1, 4):
#     print(f'это i {i}')

#     for j in range(11):
#         print(f'это j {j}')
#         if j == 3:
#             break
#         if i == 2:
#                 break

# else в циклах  -> проверяет, был ли произведен выход из цикла инструкцией break или 'естественным' путем. Блок кода в else выполнится только в том случае, если выход из цикла был break



# x = int(input())
# y = int(input())

# if x // y == 0:
#     res = x // y
#     print('x делится на y')
#     print("Частное: ", res)
# elif x % y:
#     rt = x % y
#     print('x не делится на y')
#     print('Остаток: ', rt)
# else:
#     print('no')

  
# x = int(input()) 
# y = int(input()) 
# if x % y != 0: 
# for i in a:
#     if type(i)not in (int, float):
#         continue
# for i in a:
#     if type(i)not in (int, float):
#         continue
#     sum_ += i
# print(sum_)
# for i in a:
#     if type(i)not in (int, float):
#         continue
#     sum_ += i
# print(sum_)



# for i in range(1, 4):
#     print(f'это i {i}')

#     for j in range(11):
#         print(f'это j {j}')
#         if j == 3:
#             break
#         if i == 2:
#                 break

# else в циклах  -> проверяет, был ли произведен выход из цикла инструкцией break или 'естественным' путем. Блок кода в else выполнится только в том случае, если выход из цикла был break



# for i in range(1, 4):
#     print(f'это i {i}')

#     for j in range(11):
#         print(f'это j {j}')
#         if j == 3:
#             break
#         if i == 2:
#                 break

# else в циклах  -> проверяет, был ли произведен выход из цикла инструкцией break или 'естественным' путем. Блок кода в else выполнится только в том случае, если выход из цикла был break




# for i in range(1, 4):
#     print(f'это i {i}')

#     for j in range(11):
#         print(f'это j {j}')
#         if j == 3:
#             break
#         if i == 2:
#                 break

# else в циклах  -> проверяет, был ли произведен выход из цикла инструкцией break или 'естественным' путем. Блок кода в else выполнится только в том случае, если выход из цикла был break

#     print ('x не делится на y') 
#     print ('Частное: ', x // y) 
#     print ('Остатое: ', x % y) 
# else: 
#     print('х делится на у') 
#     print('Частное: ', x/y)

# name_of_list = ['Helloworld!']
# string = name_of_list[0]
# half = len(string) //2

# if len(string) % 2:
#     half+= 1

# new_list = []

# new_list += string[half:] + string[:half]
# print(new_list)

a = {'a': 1, 'b': 2, 'c': 3} 
for k,v in v.items():
    print(a)