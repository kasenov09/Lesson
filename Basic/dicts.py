''' ============ Словари (dict) ============== '''
# изменяемый тип данных, неиндексируемый, упорядоченный, итерируемый тип данных

# {ключ: значение}

# {}
''' Способы создания словарей '''
# dict_ = {}
# print(type(dict_))
# dict_1 = dict()
# print(type(dict_1))

# dict_1 = dict(a= 'hello', b=1)
# print(dict_1)

# dict_ = dict([('key', 'value')])
# print(dict_)

# ключи должны быть неизменяемым типом данных

# {[]: 1} TypeError: unhashable type: 'list'

# ключи -> должны быть уникальными
# a = {1: 'hello', 1: 'world', 1: '1'}
# print(a)

# значения могут быть любого типа данных

# dict_ = {
#     'name': 'Alina',
#    'last_name': None,
#     'email': True,
#    'info': [1, 2, 3, 4]
#  }
# print(dict_['name'])

# print(dict_['info'])  # получение значения по ключу
# dict_['email'] = 'test@gmail.com' # изменение значения по ключу
# print(dict_)
# dict_['email1']  ошибка
# dict_['email1'] = 12
# print(dict_)

# key, value = 'ab'
# print(key, value)

# dict_ = dict('12', 'ab', 'ad')
# print(dict_)

''' ========== Методы словарей ============'''

# dict.items() -> возвращает все пары в словаре в виде списка с кортежами
# print(dict_.items()

# a, b, c = (1, 2, 3)
# print(a, '--->', b, '--->', c)

# for key, value in dict_.items():
#     print(key, '--->', value)

# dict.values() -> используется для получения всех значений в словаре

# print(dict_.values())

# for i in dict_.values():
#     print(i)

# dict.keys() -> для получения всех ключей словаря

# print(dict_.keys())

# for i in dict_.keys():
#     print(i)

# dict.clear() -> используется для очищения словаря

# dict_.clear()
# print(dict_)

# del dict_ -> удаляет объект
# print(dict-)

# dict.copy() -> возвращает копию словаря
# dict_copy = dict_.copy()
# print(dict_copy)

# dict.fromkeys(seq, [default]) -> создает словарь с ключами из последовательности и значением default (None)

# list_ = ['name', 'hello', 'test']
# dict_ = dict.fromkeys(list_, 1)
# print(dict_)

# dct = dict.fromkeys('as')
# print(dct)

# dict.get(key, [default]) -> возвращает значение по ключу, если такого ключа нет , не бросает исключение, а возвращает default, если default не указан возвращает None

# dict[key] -> бросает исключение, если такого ключа нет (вызывает ошибку)

# dict_ = {1: 'one', 2: 'two'}
# print(dict_.get(1)) # one
# print(dict_.get(3,'no such key'))  # 'no such key'
# print(dict_.get(3)) # None

# dict.update(new_dict) -> добавляет new_dict в наш словарь

dict_= {1: 'one', 2: 'two'}
dict_.update({3: 'three', 4: 'four'})
# new_dict = {5: 'five', 6: 'six'}
# dict_.update(new_dict)
print(dict_)

# dict.setdefault(key, [default_value]) -> 
# 1. Работает как get
# 2. если ключа нет , создает новую пару key: default_value, если не указать default_value -> None

# dict_= {1: 'one', 2: 'two'}
# print(dict_.setdefault(2)) # two

# print(dict_.setdefault(3, 'three')) # three
# print(dict_.setdefault(4)) # None

''' Удаление элементов словаря '''
# dict.pop(key, [message]) -> удаляет пару ключ, значение и возвращает значение, если нет выводит message (по умолчанию бросает исключение)


# dict_= {1: 'one', 2: 'two', 3: 'three'}
# deleted = dict_.pop(1)
# print(dict_)
# print(dict_, deleted)
# print(dict_.pop(4)) # KeyError: 4
# print(dict_.pop(4, 'no such key')) # no such key

# dict.popitem() -> удаляет последнюю пару ключ и значение и возвращает его

# print(dict_.popitem()) # (3, 'three')
# print(dict_)

''' Поменять местами ключи и значения '''
# new_dict = {}
# for key, value in dict_.items():
#  )   new_dict.update({value: key})

# print(new_dict)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# numbers2 = list(numbers)
# print(numbers)

# dict_= {1: 'one', 2: 'two', 3: 'three'}
# deleted = dict_.pop(1, 2)
# print(dict_)
# print(dict_, deleted)
# print(dict_.pop(4)) # KeyError: 4
# print(dict_.pop(4, 'no such key')) # no such key
list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
repeats = 3
res= []
for i in list_:
    sum = 0
    for j in list_:
        if i == j:
            sum +=1
            if sum >=repeats:
                res.append(i)
res.reverse()
res = list(set(res))
print(res)