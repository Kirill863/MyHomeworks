print()
print('# Операции над множествами')
set1 = {'apple', 'banana', 'cherry'}
set2 = {'cherry', 'melon', 'peach'}
print('# объединение |')
print(set1)
print(set2)
print(set1 | set2)  # {'peach', 'cherry', 'melon', 'apple', 'banana'}
print(set1.union(set2))  # {'peach', 'cherry', 'melon', 'apple', 'banana'}

print('# пересечение &')
print(set1)
print(set2)
print(set1 & set2)  # {'cherry'}
print(set1.intersection(set2))  # {'cherry'}

print('# симметричная разность ^')
print(set1)
print(set2)
print(set1 ^ set2)  # {'peach', 'banana', 'melon', 'apple'}
print(set1.symmetric_difference(set2))  # {'peach', 'banana', 'melon', 'apple'}

print('# разность set1 - set2')
print(set1)
print(set2)
print(set1 - set2)  # {'banana', 'apple'}
print(set1.difference(set2))  # {'banana', 'apple'}

print('# разность set2 - set1')
print(set1)
print(set2)
print(set2 - set1)  # {'peach', 'melon'}
print(set2.difference(set1))  # {'peach', 'melon'}

print()
set1 = {'apple', 'banana', 'cherry'}
set2 = {'cherry', 'melon', 'peach'}
set1.update(set2)  # аналог .union(), но с изменением множества set1
print(set1)

print()
set1 = {'apple', 'banana', 'cherry'}
set2 = {'cherry', 'melon', 'peach'}
set1.intersection_update(set2)  # аналог .intersection(), но с изменением множества set1
print(set1)

print()
set1 = {'apple', 'banana', 'cherry'}
set2 = {'cherry', 'melon', 'peach'}
set1.symmetric_difference_update(set2)  # аналог .symmetric_difference(), но с изменением множества set1
print(set1)

print()
set1 = {'apple', 'banana', 'cherry'}
set2 = {'cherry', 'melon', 'peach'}
set2.difference_update(set1)  # аналог .difference(), но с изменением множества set1
print(set2)

print()
set1 = {'apple', 'banana', 'cherry'}
set2 = {'cherry', 'melon', 'peach'}
set1.difference_update(set2)  # аналог .difference(), но с изменением множества set1
print(set1)
