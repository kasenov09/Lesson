# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}

# for k,v in a.items():
#     print(k,v)


# # a['apple']=a['apple']/5
# # a['orange']=a['orange']/5
# # a['banana']=a['banana']/5
# # print(a)

# for k, v in a.items():
#     a[k] = v/5
# print(a)

# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# for k, v in a.items(): 
#     if v % 2 == 0: 
#         del a[k] 
# print(a)
# list_ = ['world','hello']
# new_list = [list_[1], list_[0]]
# print(new_list)
# suitcase = []
# suitcase.append('dd')
# suitcase.append('ff')
# suitcase.append('aa')
# suitcase.append('ss')
# suitcase.append('hh')
# suitcase.pop()
# suitcase.insert(0, 'ee')
# print(suitcase)

# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# for res in nums:
#     if res < 5:
#         print(str(res))

# x = int(input())
# y = int(input())
# if x % y == 0:
#     print('x делится на y',
#           'частное: ', x // y)
# a= 0
# while a!= 11:
#     a+=1
#     print(a)
#     if a == 5:
#         continue
list_ = [1, 2, 3, 4, 5] 
if list_ % 2 == 0: 
    print('четное') 
else: 
    print('нечетное' )