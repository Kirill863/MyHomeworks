# Тема: Основные методы строк
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Преобразуйте строку "hOw aRe yOu?" в верхний регистр.
# Ожидаемый результат: "HOW ARE YOU?"
print("hOw aRe yOu?".upper())

# 2. Посчитайте количество символов "a" в строке "Bananas are amazing!".
print("Bananas are amazing!".count('a'))

# 3. Преобразуйте строку "PYTHON PROGRAMMING" в нижний регистр.
# Ожидаемый результат: "python programming"
print("PYTHON PROGRAMMING".lower())

# 4. Удалите начальные пробелы из строки "   Discover new worlds   ".
# Ожидаемый результат: "Discover new worlds   "
print("   Discover new worlds   ".lstrip())

# 5. Замените "rainy" на "sunny" в строке "It was a rainy day.".
# Ожидаемый результат: "It was a sunny day."
print("It was a rainy day.".replace('rainy','sunny'))

# 6. Найдите индекс подстроки "innovation" в строке "Innovation drives progress.".
print('Innovation drives progress.'.index('Innovation'))

# 7. Удалите конечные пробелы из строки "   Explore the universe   ".
# Ожидаемый результат: "   Explore the universe"
print('   Explore the universe   '.rstrip())

# 8. Найдите индекс подстроки "galaxy" в строке "The Milky Way galaxy is vast.".
print('he Milky Way galaxy is vast.'.index('galaxy'))

# 9. Разделите строку "Apple;Banana;Cherry;Date" по точке с запятой.
# Ожидаемый результат: ["Apple", "Banana", "Cherry", "Date"]
print('Apple;Banana;Cherry;Date'.split(';'))

# 10. Замените "robots" на "humans" в строке "In the future, robots will rule the world.".
# Ожидаемый результат: "In the future, humans will rule the world."
print('In the future, robots will rule the world.'.replace('robots','humans'))

# 11. Преобразуйте строку "artificial intelligence" в заглавный регистр.
# Ожидаемый результат: "Artificial Intelligence"
print('artificial intelligence'.title())

# 12. Разделите строку "Python is a versatile language" по пробелам.
# Ожидаемый результат: ["Python", "is", "a", "versatile", "language"]
print('Python is a versatile language'.split(' '))

# 13. Удалите начальные и конечные пробелы из строки "   Learn Python   ".
# Ожидаемый результат: "Learn Python"
print('   Learn Python   '.strip())

