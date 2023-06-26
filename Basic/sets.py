''' Множества -> set()'''

# неизменяемый, неупорядоченный, неиндексируемый,  итерируемый тип данных, который хранит в себе только уникальный значения

''' создание пустого множества '''
# set_a = set()
# print(type(set_a))
# set_b = {1, 2, 3}
# print(set_b)
 
'''Элементами множества могут быть только неизменяемые типы данных'''

# set_ = set({1: 'a', 2: 'b', 3: 'c'})
# print(set_)
# set_ = set([1, 2, 3, 4, 5,21, 1, 2])
# print(set_)
# set_ = set('Makjdoomm')
# print(set_)

''' Методы множеств '''

# set.add(element) -> добавляет element во множество
''' если добавляем tuple, то все его элементы должны быть неизменяемыми'''
# set_a = {1, 2, 3, 4, (1, 2,)}
# set_a.add('hello')
# print(set_a)

# set.update(seq) -> добавляет элементы из последовательности во множество

# set_a = {1, 2, 3, 4, (1, 2,)}
# set_a.update([1, 2, 3, 'Makers'])
# print(set_a)

# set.clear() -> очищает множество

# set_a = {1, 2, 3, 4, (1, 2,)}
# set_a.clear()
# print(set_a)

# set.pop() -> удаляет рандомный элемент из множества, первый в текущем порядке
# set_a = {1, 2, 3, 4, (1, 2,)}
# set_a.pop()
# print(set_a)

# set.difference (other_set) -> возвращает элементы , которые есть в set_a но нет в set_b

# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 9}
# print(set_a - set_b)
# print(set_a.difference(set_b))


# set_a.symmetric_difference(set_b) -> возвращает уникальные элементы для set_a и set_b 

# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 9}
# print(set_a.symmetric_difference(set_b))
# print(set_a ^ set_b)

# set_a.intersection(set_b) -> возвращает схожие элементы обоих множеств

# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 9}
# print(set_a.intersection(set_b))
# print(set_a & set_b)

# set_a.union(set_b) ->  соединяет два множества

# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 9}
# print(set_a.union(set_b))
# print(set_a | set_b)

''' 
set.difference_update()
set.intersection_update()
set.symmetric_update()
set.isdisjoint()
set.issuperset()
set.issubset()
'''
# a =  {0, 1, 2, 3, 34, 5, 8, 13} 
# b =  {1, 2, 34}
# if a.issuperset(b):
#     print('Надмножество!')

# ingredients = {"cыр чеддар","грибы", "Колбаса", "соус","шпинат"} 
# ingredients.add('помидор')
# ingredients.discard("Колбаса")
# ingredients.remove("шпинат")
# ingredients.add("базилик")
# ingredients.remove("cыр чеддар")
# ingredients.add("сыр моцарелла")
# print(ingredients)


# a = [set(),set(),set()]
# inp = int(input())
# inp2 = int(input())
# if inp2 == 1:
#     a[0].add(inp)
# print(inp)
# elif if inp2 == 2:
#     a[1].add("default value")
#         print(inp)

# elif if inp2 == 3:
#     a[2].add("default value")

# print(inp)

# else:
#     print(none)

# a = [set(), set(), set()]
# inp = input()
# inp2 = int(input())

# if inp2 == 1:
#     a[0].add(inp)
#     print(inp)
# elif inp2 == 2:
#     a[1].add("default value")
#     print(a[1])
# elif inp2 == 3:
#     a[2].add("default value")
#     print(a[2])
# else:
#     print("none")a


# numbers = []  # Список для хранения введенных чисел

# n = int(input("Сколько чисел вы хотите ввести? "))

# for i in range(n):
#     number = int(input("Введите число: "))
#     numbers.append(number)

# max_number = max(numbers)  # Находим м аксимальное число в списке

# print("Наибольшее натуральное число:", max_number)

# a = [set(),set(),set()]





# inp1 = input()
# inp2 = int(input())
# if inp2 == 1:
#     a[0].add(inp1)
#     a[1].add("default value")
#     a[2].add("default value")
# elif inp2 == 2:
#     a[0].add("default value")
#     a[1].add(inp1)
#     a[2].add("default value")
# elif inp2 == 3:
#     a[0].add("default value")
#     a[1].add("default value")
#     a[2].add(inp1)
# else:
#     a[0].add("default value")
#     a[1].add("default value")
#     a[2].add("default value")

# print(a)