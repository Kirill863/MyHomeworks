# спецсимволы и экранирование
print('# спецсимволы и экранирование')
print("Hello world!")
print('Hello world!')

# print('Let's go!')  # SyntaxError: unterminated string literal (detected at line 6)
print("Let's go!")  # Let's go!

# print("She said: "YES"")  # SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('She said: "YES"')


# экранирование
print('# экранирование')
print("Let\'s go!")
print('Let\'s go!')
print("She said: \"YES\"")
print('She said: "YES"')
print('\\ слэш это символ для экранирования специальных символов')

# слэш не воспринимается как отдельный символ, это знак экранирования
print(len("Let's go!"))  # 9
print(len('Let\'s go!'))  # 9


# спецсимволы
# \n - перенос строки
# \t - табуляция
print('# спецсимволы')
print('Hello \nworld!')
print('Hello \tworld!')


# f-строки
print('# f-строки')
x = 5
y = 19
print(f'x = {x}, y = {y}')
print(f'{x = }, {y = }')
print('# форматирование чисел')
pi = 3.14159265
print(f'pi = {pi:.2f}')
print(f'pi = {pi:.4f}')
print(f'pi = {pi:.8f}')
print('# выравнивание')
print(f'{x:4}')
print(f'{y:4}')
print(f'{178:4}')
