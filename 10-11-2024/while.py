# цикл while
# while условие:
#     тело цикла

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# i, j, k — нормальные названия для абстрактных переменных цикла

# password = ''
# while password != 'secret':
#     password = input('Enter password: ')

# break - выход из цикла
# continue - переход к следующей итерации
# else - выполняется после завершния цикла, если не было выплнения break

# break
# while True:
#     password = input('Enter password: ')
#     if password == 'secret':
#         print('Пароль верный')
#         break
#     if password == 'exit':
#         print('Вы вышли из программы')
#         break
#     print('Пароль неверный')

# continue
# i = 0
# while i < 100:
#     i += 1
#     if i % 2 == 0:
#         continue  # когда i % 2 == 0, то переходим к следующей итерации
#     print(i)

# data = input('Enter data: ')
# if data:
#     print('Вы что-то ввели')
# else:
#     print('Вы ничего не ввели')

# := walrus operator, моржовый оператор
# if data := input('Enter data: '):
#     print('Вы что-то ввели')
# else:
#     print('Вы ничего не ввели')

# word = ''
# while word != 'soft_stop':
#     word = input('Введите слово: ')
#     if word == 'STOP':
#         print('Цикл остановлен с помощью оператора break')
#         break
# else:  # этот else относится к while, не к if
#     print('Цикл был выполнен полностью и был запущен оператор else')

# print('Этот print выполнится в любом случае')

# while (word := input('Введите слово: ')) != 'soft_stop':
#     if word == 'STOP':
#         print('Цикл остановлен с помощью оператора break')
#         break
# else:  # этот else относится к while, не к if
#     print('Цикл был выполнен полностью и был запущен оператор else')

# print('Этот print выполнится в любом случае')
