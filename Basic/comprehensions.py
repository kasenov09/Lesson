'''============Comprehension============== '''
# генератор последовательности в одну строку


# for переменная in диапозон:
#      тело
# Синтаксис
#1. результат for элемент in итерируемый объект
#2. результат for элемент in итерируемый объект if фильтрация


'''========List comprehension========'''
# упрощение процесса создания списков


# list_ = []
# for i in 'hello':
#     list_.append(i)

# print(list_)

# list_0 = list((i for i in 'hello'))
# print(list_0)

# list_ = [i for i in 'hello']
# print(list_)


# import time
# start_time = time.time()

# list_ = [i for i in range(1, 11) if i % 2 == 0]
# print(list_)

# list_ = [i for i in range(2, 11, 2)]
# print(list_)

# list_ = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         list_.append(i)
# print(list_)


# print(['hello' for i in range(10)])

# print([input() for i in range(10)])


# [элемент if условие else элемент 2 for i in итерируемый объект]

# a = ['четное' if i % 2 == 0 else 'нечетное' for i in range(1,11)]
# print(a)

# list_str = []
# for i in range(1,11):
#     if i % 2 == 0:
#         list_str.append('четное')
#     else:
#         list_str.append('нечетное')

# print(list_str)

# a = [
#     'четное'
#     if i % 2 == 0
#     else 'нечетное'
#     for i in range(1, 11)
#     ]
# print(a)

'''=========== Set comprehension ============='''

# list_ = [1, 2, 3, 4, 5, 6, 1, 3, 2]
# set_l = {i for i in list_}
# print(set_l)

# set_ = set()
# for i in list_:
#     set_.add(i)

# print(set_)

# list_ = [1,'test', 2, 3, 4,'World', 5, 6, 1, 3, 2]
 # set_l = {i + ' world' for i in list_ if  type(i) == str }
# print(set_l)


# list_ = [1,'test', 2, 3, 4,'World', 5, 6, 1, 3, 2]
# set_l = {i + ' world' if  type(i) == str else i + 1 for i in list_ }
# print(set_l)

'''=============== Dict comperension =============='''

# dict_ = {1: 'a', 2: 'b', 3: 'c'}

# dict1 = {}
# for k, v in dict_.items():
#     dict1.update({v: k})

# print(dict1)

# dict2 = {v: k for k, v in dict_.items()}
# print(dict2)

# dict_ = {i: i ** 2 for i in range(1,11)}
# print(dict_)


# list_ = [1, 2, 3, 1, 4, 5, 3, 5, 7]
# dict_1 = {i: list_.count(i) for i in list_}
# print(dict_1)

# dict_ = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# dict_1 = {k:('четное' if v % 2 == 0 else 'нечетное') for k, v in dict_.items()}
# print(dict_1)

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']
# dict_ = {
#         list1[index]: list2[index] 
#        for index in range(len(list1))
#        }

# print(dict_)


'''============ Вложенные comprehensions ============='''

# dict_ = {i: 
#          [j for j in range(1, i+1)] 
#          for i in range(1,6)
#          }
# print(dict_)

# list_ = [['hello world' for i in range(2)] 
#          for i in range(3)
#          ] 
# print(list_)

# employees = {
#     'id1': {
#         'first name': 'Александр',
#         'last name' : 'Иванов',
#         'age': 30,
#         'job':'программист'
#             },
#     'id2': {
#         'first name': 'Ольга',
#         'last name' : 'Петрова',
#         'age': 35,
#         'job':'ML-engineer'
#             }
#         }

# dct = {
#     key: 
#     {k: float(v) 
#     if k == 'age' else v 
#     for k, v in value.items() 
#     } 
#     for key,value in 
#     employees.items()
#     }

# print(dct)

# for info in employees.values():
#     for k, v in info.items():
#         if k == 'age':
#             info[k] = float(v)

# print(employees)



# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4] 
# int_list = [i if i >= 0 else 1 for i in list_] 
# print(int_list)



# list_ =[i**2 for i in range(25) ] 
# print(list_)
str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
int_list = [i for i in str_list]
print(int_list)